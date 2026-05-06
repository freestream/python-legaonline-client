# AGENTS.md — lega_soap

Agent-facing reference for the `lega_soap` Python package. Covers what matters most when reading, writing, or debugging this codebase. Does not duplicate README.md.

---

## What This Library Does

Typed Python SOAP client for the **LegaOnline rental management system**. Wraps two WSDL endpoints:

| Client | Endpoint | Covers |
|--------|----------|--------|
| `Client` | `rentalapi.asmx` | Customers, reservations, orders, occasions, objects, jobs, catalog, shipping, etc. |
| `FinancialClient` | `financialapi.asmx` | Invoices, payments, customer financial data, account settings |

Both clients authenticate independently — tokens are not shared.

---

## Installation

```bash
pip install -e .          # dev
pip install -e ".[dev]"   # dev + pytest
```

---

## Common Use Cases

### 1. Fetch customers with filtering

```python
from lega_soap.client import Client
from lega_soap.auth import Credentials
from lega_soap.query import FilterSpec, SortSpec

client = Client(creds=Credentials(user_id=123, hash="your-hash"), authenticate_on_init=True)

filters = FilterSpec.from_tuples(
    ("CustomerID", "=", "1001"),
    ("Status", "!=", "inactive"),
)
sorting = SortSpec.from_tuples(("CustomerID", "asc"))

result = client.customers.get_customer(filtering=filters, sorting=sorting)
```

### 2. Create or update a reservation (upsert)

`set_reservation` is an upsert — pass `reservation_id=None` to create, or an existing ID to update.

```python
import datetime as dt
from zoneinfo import ZoneInfo

result = client.reservations.set_reservation(
    customer_id=1001,
    customer_contact_id=5,
    period_start=dt.datetime(2026, 6, 1, 8, 0, tzinfo=ZoneInfo("Europe/Stockholm")),
    period_end=dt.datetime(2026, 6, 7, 17, 0, tzinfo=ZoneInfo("Europe/Stockholm")),
)
```

### 3. Cancel reservations by ID list

```python
from lega_soap.query import IntListSpec

ids = IntListSpec.from_list([101, 102, 103])
client.reservations.cancel_reservation(reservation_ids=ids)
```

### 4. Build XML for methods that require XML string params

Some SOAP methods (e.g. `set_job_attributes`) accept an XML string, not a dict. Use `XmlNode` / `XmlArray`:

```python
from lega_soap.query import XmlArray, XmlNode

attrs = XmlArray(
    wrapper_tag="JobAttributes",
    item_tag="JobAttribute",
    items=[XmlNode("JobAttribute", {"AttributeID": 1, "Value": "foo"})],
)
client.jobs.set_job_attributes(job_attribute=attrs.to_xml())
```

### 5. Use the Financial API

```python
from lega_soap.financial_client import FinancialClient
from lega_soap.auth import Credentials

fc = FinancialClient(creds=Credentials(user_id=123, hash="your-hash"))
invoices = fc.invoices.get_invoice_v4(filtering=filters)
```

---

## Architecture in Brief

```
Client / FinancialClient
  └── BaseService._call(method_name, *args, **kwargs)
        1. ensure_valid_token()         ← SOAP round-trip if token invalid
        2. filter out _EMPTY kwargs     ← None, "", [], {}, () silently dropped
        3. zeep SOAP call
        4. serialize_object()
        5. sanitize_object()            ← applies tzinfo to all datetimes, extracts _raw_elements
```

Services are thin wrappers — no business logic lives in the service layer.

---

## Non-Obvious Behaviour

- **`FilterSpec.from_tuples` tuple order is `(field, condition, value)`** — not `(field, value, condition)`. Easy to get wrong silently.
- **`ensure_valid_token()` makes a SOAP call every time** (calls `ValidateAuthToken`). It re-authenticates if invalid. This is a network round-trip per service call.
- **`_EMPTY` silently drops kwargs**: any kwarg whose value is `None`, `""`, `[]`, `{}`, or `()` is stripped before the SOAP call. If the API requires a literal null, pass it as a positional arg instead.
- **`Set*` methods are upserts** — `SetCustomer`, `SetReservation`, `SetJob` etc. create if no ID given, update if ID present.
- **`IntListSpec.to_zeep()`** returns `{"int": [...]}` for zeep `ArrayOfInt` params. **`IntListSpec.to_xml()`** returns raw `<int>...</int>` XML for inline XML params. They are not interchangeable.
- **Fields missing from WSDL schema** end up in `_raw_elements` (lxml elements). `sanitize_object` extracts them — but only populates a key if the serialized value is `None`. New API fields not yet in the WSDL will appear this way.
- **Naive datetimes get `tzinfo` assigned** (not converted). Aware datetimes are converted to the target tz via `.astimezone()`. Default tz order: `TZ` env var → system local → UTC.
- **All classes use `__slots__`** — dynamic attribute assignment will raise `AttributeError`.
- **Zeep is configured `strict=False, xml_huge_tree=True`** — lenient parsing, handles large SOAP responses.
- **`paymentMetodID`** (single `h`) in `create_reservation_inc_payment_method` is a typo preserved from the WSDL. Do not fix it.

---

## Error Types

| Exception | When raised |
|-----------|-------------|
| `LegaError` | Base; inherit from `RuntimeError` |
| `AuthError` | `GetAuthToken` fails or returns empty token |
| `ServiceError` | SOAP method not found (`"SOAP method not found: X"`) or call fails (`"X failed: <original>"`) |

---

## Testing Without Live SOAP

Use `RecordingZeepService` from `tests/conftest.py` — intercepts any attribute access and records calls:

```python
from tests.conftest import RecordingZeepService, FakeZeepClient
from tests.helpers import FakeAuth
from lega_soap.services.reservation import ReservationService
from zoneinfo import ZoneInfo

svc = ReservationService(RecordingZeepService(), FakeAuth(), ZoneInfo("Europe/Stockholm"))
svc.cancel_reservation(reservation_ids=IntListSpec.from_list([1, 2]))
```
