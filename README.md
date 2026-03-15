# LegaOnline SOAP API client for python

A typed, class-based Python SOAP client for the **LegaOnline SOAP
API**.

This library wraps the LegaOnline SOAP WSDL using `zeep` and provides:

-   Centralized authentication with token handling
-   Service-based structure (one class per API domain)
-   Typed query builders (FilterSpec, SortSpec, IntListSpec)
-   Dynamic XML builders for complex SOAP payloads
-   Automatic response serialization and sanitization
-   Fully testable architecture (no live SOAP dependency required)

------------------------------------------------------------------------

## Installation

``` bash
pip install -e .
```

Dependencies:

-   zeep
-   requests

------------------------------------------------------------------------

## Quick Example

``` python
from lega_soap.client import Client
from lega_soap.auth import Credentials
from lega_soap.query import FilterSpec

client = Client(
    creds=Credentials(user_id=123, hash="your-hash"),
    authenticate_on_init=True,
)

filters = FilterSpec.from_tuples(
    ("CustomerID", "=", "1001"),
)
customer = client.customers.get_customer(filtering=filters)
print(customer)
```

------------------------------------------------------------------------

## Architecture

    Client
     ├── auth
     ├── account
     ├── availability
     ├── calendar
     ├── catalog
     ├── communication
     ├── customers
     ├── geo
     ├── integration
     ├── jobs
     ├── misc
     ├── objects
     ├── occasions
     ├── orders
     ├── report
     ├── reservations
     └── shipping

Each domain has its own service class.

Example:

``` python
client.customers.get_customer(...)
client.orders.calculate_prices(...)
client.occasions.get_occasion(...)
```

All SOAP calls flow through a shared `_call()` method which:

1.  Injects the auth token
2.  Executes the zeep method
3.  Serializes the result
4.  Sanitizes datetime objects

------------------------------------------------------------------------

## Authentication

Authentication happens automatically when:

``` python
Client(authenticate_on_init=True)
```

Or manually:

``` python
client.auth.authenticate()
```

The token is stored centrally and injected into every SOAP call.

------------------------------------------------------------------------

## Filtering & Sorting

### FilterSpec

``` python
from lega_soap.query import FilterSpec

filters = FilterSpec.from_tuples(
    ("Status", "=", "active"),
    ("OccasionID", "in", "12,13"),
)

xml = filters.to_xml()
```

### SortSpec

``` python
from lega_soap.query import SortSpec

sorting = SortSpec.from_tuples(
    ("OccasionID", "asc"),
    ("Status", "desc"),
)

xml = sorting.to_xml()
```

------------------------------------------------------------------------

## Integer Lists

Used for operations that take a list of IDs, such as `cancel_occasion` or `delete_customer_contact`.

``` python
from lega_soap.query import IntListSpec

ids = IntListSpec.from_list([10, 11, 12])

client.occasions.cancel_occasion(occasion_ids=ids)
```

Internally, `.to_zeep()` converts the list to the `{"int": [...]}` format that zeep expects for `ArrayOfInt` SOAP parameters.

------------------------------------------------------------------------

## Dynamic XML Builder

Some SOAP methods accept XML string parameters (e.g. `set_job_attributes`, `update_external_account_user`).

Use `XmlNode` and `XmlArray` to build these strings.

### Example: SetJobAttributes

``` python
from lega_soap.query import XmlArray, XmlNode

attrs = XmlArray(
    wrapper_tag="JobAttributes",
    item_tag="JobAttribute",
    items=[
        XmlNode("JobAttribute", {"AttributeID": 1, "Value": "foo"}),
    ],
)

client.jobs.set_job_attributes(job_attribute=attrs.to_xml())
```

------------------------------------------------------------------------

## Timezone Handling

All datetime objects in responses are automatically converted to the
configured timezone.

You can override timezone on client creation:

``` python
from zoneinfo import ZoneInfo

client = Client(
    creds=Credentials(...),
    tzinfo=ZoneInfo("Europe/Stockholm"),
)
```

------------------------------------------------------------------------

## Testing

Run tests:

``` bash
pytest
```

The project is designed to be fully testable without live SOAP calls.

------------------------------------------------------------------------

## Design Principles

-   Explicit SOAP method names
-   Explicit WSDL parameter names
-   Strong typing where practical
-   Dynamic XML where necessary
-   Services are thin wrappers over SOAP operations
-   Business logic does not live in service layer
