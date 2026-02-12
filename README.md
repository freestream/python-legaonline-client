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
-   pytz (or zoneinfo if Python ≥ 3.9)

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
    ("CustomerID", "1001", "="),
)
customer = client.customer.get_customer(filtering=filters)
print(customer)
```

------------------------------------------------------------------------

## Architecture

    Client
     ├── auth
     ├── customer
     ├── order
     ├── occasion
     ├── account
     └── ...

Each domain has its own service class.

Example:

``` python
client.customer.get_customer(...)
client.order.calculate_prices(...)
client.occasion.get_occasion(...)
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
client.authenticate()
```

The token is stored centrally and injected into every SOAP call.

------------------------------------------------------------------------

## Filtering & Sorting

### FilterSpec

``` python
from lega_soap.query import FilterSpec

filters = FilterSpec.from_tuples(
    ("Status", "active", "="),
    ("OccasionID", "12,13", "in"),
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

## Integer List XML

Used for operations like `DeleteCustomerContactAttribute`.

``` python
from lega_soap.query import IntListSpec

ids = IntListSpec.from_list([10, 11, 12])
xml = ids.to_xml()
```

Produces:

``` xml
<int>10</int><int>11</int><int>12</int>
```

------------------------------------------------------------------------

## Dynamic XML Builder

Some SOAP methods require nested XML structures.

Use `XmlNode` and `XmlArray`.

### Example: CalculatePrices

``` python
from decimal import Decimal
from lega_soap.query import XmlArray, XmlNode

answer_prices = XmlArray(
    wrapper_tag="AnswerPriceInfo",
    item_tag="AnswerPriceInfo",
    items=[
        XmlNode("AnswerPriceInfo", {
            "AnswerID": 1,
            "Price": Decimal("99.50"),
        }),
        XmlNode("AnswerPriceInfo", {
            "AnswerID": 2,
            "Price": Decimal("0"),
        }),
    ],
)

response = client.order.calculate_prices(
    object_id=10,
    answer_price_info=answer_prices,
)
```

------------------------------------------------------------------------

## Strongly Typed Variant (Optional)

You may also use structured helper models:

``` python
from lega_soap.query import AnswerPriceInfo
from lega_soap.query import XmlArray

items = [
    AnswerPriceInfo(answer_id=1, price=100),
    AnswerPriceInfo(answer_id=2, price=0),
]

xml_array = XmlArray(
    wrapper_tag="AnswerPriceInfo",
    item_tag="AnswerPriceInfo",
    items=[item.to_xml_node() for item in items],
)
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
