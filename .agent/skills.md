# lega_soap — Agent Skills Reference

Deep-dive patterns, error handling, auth flows, and API pitfalls. For high-level overview see `AGENTS.md`.

---

## Auth Flow (Full Detail)

```python
# AuthManager state machine
AuthManager.authenticate()
    → calls GetAuthToken(user_id, hash_)
    → stores token in self._token
    → raises AuthError if result is falsy

AuthManager.ensure_valid_token()
    → calls ValidateAuthToken(token)         ← network call every time
    → if invalid: re-calls authenticate()
    → returns valid token string
```

`ensure_valid_token()` is called inside `BaseService._call()` on every SOAP method invocation. There is no in-process token caching beyond the stored string — every call validates over the network.

`FinancialClient` creates its own `AuthManager` against `financialapi.asmx`. The token from `Client` (rental API) is separate and not reusable.

---

## Request Pipeline (Code-Level)

```python
# BaseService._call internals
def _call(self, method_name, *args, **kwargs):
    token = self._auth.ensure_valid_token()          # 1. SOAP round-trip
    method = getattr(self._service, method_name)     # 2. raises ServiceError if missing
    filtered_kwargs = {k: v for k, v in kwargs.items()
                       if v not in (None, "", [], {}, ())}  # 3. drop _EMPTY
    result = method(token, *args, **filtered_kwargs) # 4. token prepended to args
    serialized = serialize_object(result)            # 5. zeep → dict/list
    return sanitize_object(serialized, self._tzinfo) # 6. tz + _raw_elements
```

The token is always the **first positional argument** to the underlying SOAP method. Services must not pass it manually.

`BaseServiceNoAuth._call_noauth` skips step 1 and does not prepend token in step 4.

---

## Query DSL Patterns

### FilterSpec

```python
# Tuple order: (field, condition, value)
FilterSpec.from_tuples(
    ("CustomerID", "=", "1001"),
    ("Status", "in", "active,pending"),   # comma-separated string for "in"
    ("Created", ">=", "2026-01-01"),
)

# Allowed conditions (and their aliases):
# "=", "eq"   |  "!=", "ne"  |  ">", "gt"
# "<", "lt"   |  ">=", "gte"/"ge"  |  "<=", "lte"/"le"
# "in"

# Produces: <Filtering><Filter><FilterName>...</FilterName>...</Filter></Filtering>
# Empty FilterSpec.to_xml() returns "" (safe to pass to _call)
```

**Common mistake**: passing `(field, value, condition)` instead of `(field, condition, value)`. No runtime error — just wrong results from the API.

### SortSpec

```python
SortSpec.from_tuples(
    ("CustomerID", "asc"),
    ("Created", "desc"),
)
# Produces: <Sorting><Sort><SortName>...</SortName><SortDirection>asc</SortDirection></Sort></Sorting>
```

### IntListSpec — two serialization modes

```python
ids = IntListSpec.from_list([10, 11, 12])

ids.to_zeep()  # → {"int": [10, 11, 12]}   ← pass to zeep ArrayOfInt kwargs
ids.to_xml()   # → "<int>10</int><int>11</int><int>12</int>"  ← inline XML string
ids.to_xml(wrap="IDs")  # → "<IDs><int>10</int>...</IDs>"

# Returns None / "" if empty
```

Services decide which form to use. Check how the service method calls `_call` to know which is correct.

### XmlNode

```python
XmlNode("Job", {
    "JobID": 1,
    "Description": "Foo & Bar",   # auto HTML-escaped
    "Active": True,               # → "true" (not "True")
    "SubNode": XmlNode(...),      # embedded as-is
    "Tags": ["a", "b"],           # → <Tags>a</Tags><Tags>b</Tags> (repeated)
    "Missing": None,              # skipped
})
```

### XmlArray

```python
XmlArray(
    wrapper_tag="JobAttributes",
    item_tag="JobAttribute",
    items=[
        XmlNode("JobAttribute", {"AttributeID": 1, "Value": "x"}),
        XmlNode("JobAttribute", {"AttributeID": 2, "Value": "y"}),
    ]
)
# → <JobAttributes><JobAttribute><AttributeID>1</AttributeID>...</JobAttribute>...</JobAttributes>

# If XmlNode.tag != item_tag, XmlArray wraps it:
# XmlArray("Outer", "Item", [XmlNode("Inner", {...})])
# → <Outer><Item><Inner>...</Inner></Item></Outer>
```

---

## Domain-Specific Spec Classes

All live in `query.py`. All are `frozen=True` dataclasses with a `.to_xml() -> XmlNode` method.

| Class | SOAP usage | Key fields |
|-------|-----------|------------|
| `AnswerPriceInfo` | `calculate_prices` | `answer_id`, `price` |
| `JobSpec` | `set_job` / `set_jobs` | `job_id`, `occasion_id`, `customer_id`, `start_date`, `end_date` |
| `OccasionAnswerSpec` | `set_occasion_answer` | `occasion_id`, `answer_id`, `value`, `quantity`, `price` |
| `OccasionLocationSpec` | `set_occasion_location` | `occasion_id`, `location_id`, `location_address_id` |
| `OccasionObjectAnswerSpec` | `set_occasion_object_answer` | `answer_id`, `occasion_id`, `object_id`, `answer_text`, `answer_time`, `answer_number` |
| `OccasionParticipantNumberSpec` | `set_occasion_participant_number` | `participant_number`, `occasion_id` |
| `OccasionQuantitySpec` | `set_occasion_quantity` | `occasion_id`, `quantity` |
| `OccasionSeatingInfoSpec` | `set_occasion_seating_info` | `occasion_id`, `seating_id` |
| `ReportParameterSpec` | `set_report_parameter` | `name`, `value` |
| `OrderInfoSpec` | shipping/order operations | full address + logistics fields |

---

## SetReservation / SetReservationV* — Upsert Pattern

```python
# Create: omit reservation_id (or pass None)
# Update: pass existing reservation_id

# V1 param key: reservation=record
# V2 param key: reservation=record  (adds ExternalReservationID)
# V3 param key: reservationV3=record  ← different kwarg name!
# V4 param key: reservation=record  (adds InvoiceNotes, Created defaults to now())

# V3 and V4 auto-default Created to dt.datetime.now() if not passed
```

---

## SetReservationAnswer — List Wrapping

```python
# set_reservation_answer sends a wrapped list:
self._call("SetReservationAnswer",
    reservationAnswerList={"ReservationAnswer": [record]})

# set_reservation_answer_v2:
self._call("SetReservationAnswerV2",
    reservationAnswerList={"ReservationAnswerV2": [record]})
```

The inner key changes between V1 and V2 — a common mistake when upgrading.

---

## _raw_elements Handling

Zeep puts XML elements not in the WSDL schema into `_raw_elements` as lxml `Element` objects. `sanitize_object` extracts them:

```python
# sanitize.py logic (simplified):
if "_raw_elements" in obj:
    extracted = {QName(elem.tag).localname: elem.text for elem in raw}
    # Only fills key if serialized value is None (doesn't overwrite known fields)
    for k, v in extracted.items():
        if sanitized.get(k) is None:
            sanitized[k] = v
```

**Implication**: fields that exist in both the schema and `_raw_elements` keep the schema value. Only schema-missing fields get populated from `_raw_elements`. Fields with `xsi:nil="true"` extract as `None`.

---

## Datetime Handling Details

```python
# sanitize_object applies target_tz recursively to all dt.datetime instances
if obj.tzinfo is None:
    return obj.replace(tzinfo=target_tz)   # assign, not convert
else:
    return obj.astimezone(target_tz)       # convert

# Default tz resolution (timezone.py):
# 1. os.environ["TZ"]
# 2. tzlocal / system local
# 3. datetime.timezone.utc
```

For response datetimes: naive datetimes from SOAP get the client's tz assigned (not converted). This means the datetime value is preserved exactly but tagged with the tz — useful for LegaOnline's responses which are typically in local server time.

For request datetimes: pass timezone-aware datetimes to avoid ambiguity. Zeep serializes them as-is.

---

## Error Handling Reference

```python
from lega_soap.exceptions import LegaError, AuthError, ServiceError

try:
    result = client.customers.get_customer(filtering=filters)
except AuthError:
    # Token auth failed — check Credentials
    pass
except ServiceError as e:
    if "SOAP method not found" in str(e):
        # Method name typo, or WSDL doesn't expose this method
        pass
    else:
        # SOAP call failed — str(e) contains "MethodName failed: <zeep error>"
        pass
```

---

## Writing Tests

```python
# Minimal test pattern
from tests.conftest import RecordingZeepService
from tests.helpers import FakeAuth
from lega_soap.services.reservation import ReservationService
from zoneinfo import ZoneInfo

zeep = RecordingZeepService()
svc = ReservationService(zeep, FakeAuth("TOKEN"), ZoneInfo("Europe/Stockholm"))

svc.cancel_reservation(reservation_ids=IntListSpec.from_list([1]))

name, args, kwargs = zeep.calls[0]
assert name == "CancelReservation"
assert args[0] == "TOKEN"                        # token is first positional
assert kwargs["reservationIDs"] == {"int": [1]}  # to_zeep() output
```

`RecordingZeepService` returns `{"ok": True, "method": name, "ts": datetime(...)}` from every call. `serialize_object` is monkeypatched to identity in conftest (`autouse=True`).

`build_required_kwargs(fn)` in `helpers.py` auto-generates dummy values for required params from type annotations — useful for smoke-test coverage of all service methods.

---

## Enums

Live in `enums.py`, re-exported from the package root (`from lega_soap import OccasionStatus`).
All are `IntEnum`, so members are usable anywhere a plain `int` is accepted.

| Enum | StatusID mapping | Used by |
|------|-----------------|---------|
| `OccasionStatus` | `1=BOOKED`, `2=PRELIMINARY`, `3=CANCELED`, `4=LOCKED` | `update_occasion_status`, `add_occasion_accessory` (the `status_id` / `StatusID` field) |

```python
from lega_soap import OccasionStatus

service.update_occasion_status(reservation_id=1, occasion_id=2, status_id=OccasionStatus.CANCELED)
```

---

## What This Library Does NOT Handle

- **Pagination**: no built-in page/offset support — callers must filter by ID ranges or dates
- **Rate limiting**: no retry or backoff — callers must implement
- **Response schema validation**: Zeep `strict=False` means unexpected fields are tolerated silently
- **Concurrent requests**: `AuthManager` has no locking — not safe for multithreaded use without external synchronization
- **Financial API auth isolation**: `FinancialClient` has its own `AuthManager`; do not pass `Client.auth` to it
- **WSDL caching**: Zeep fetches WSDL on every `Client()` instantiation unless a cached `ZeepClient` is passed
