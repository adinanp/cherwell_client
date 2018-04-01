# Cherwell
Cherwell client for python3 applications

[![PyPI version](https://badge.fury.io/py/cherwell.svg)](https://badge.fury.io/py/cherwell)
[![Updates](https://pyup.io/repos/github/adinanp/cherwell_client/shield.svg)](https://pyup.io/repos/github/adinanp/cherwell_client/)


## Usage


### Installation

Install with:
```shell
pip install cherwell
```

Or, if you're using a development version cloned from this repository:
```shell
python path-to-where-you-cloned-cherwell/setup.py install
```

### Quickstart

First, initialize a cherwell client instance

```python
from cherwell.client import CherwellClient


cherwell_client = CherwellClient('<YOUR_CHERWELL_SERVER_ADDRESS>')

```


And then, request an authentication token to use in the other requests

```python
token = cherwell_client.authenticate(
   gt=<YOUR_GRANT_TYPE>,
   cid=<YOUR_CLIENT_ID>,
   user=<YOUT_USERNAME>,
   pwd=<YOUR_PASSWORD>
)
```
With a token, you can for example create a business object.

Before, Given the cherwell API format, let's create a valid business object

```python
from cherwell.models import BusinessObject, BusinessObjectFields


data = BusinessObject('FakeBusObjectId')
data.fields = [
    BusinessObjectFields(
        fieldId='FakeFieldid',
        name='FakeFieldName',
        value='FakeFieldValue',
        dirty=True,
    ),
    BusinessObjectFields(
        fieldId='FakeFieldid2',
        name='FakeFieldName2',
        value='FakeFieldValue2',
        dirty=True,
    ),
]
```

Now, just perform

```python
bo = cherwell_client.save_business_object(token=<YOUR_TOKEN>, data=data)
```

For create/save your busines object


## Contributing

This client was made to meet a specific need of my daily life. Obviously this is very simple and does not include 100% of what the cherwell API offers.

Pull requests are welcome, as long as they follow the standards adopted and contemplate unit tests
