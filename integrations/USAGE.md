<!-- Start SDK Example Usage [usage] -->
```python
import sdk
from sdk.models import operations

s = sdk.SDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.benefits_enrollment.get_benefits_enrollment_id_(id='string')

if res.enrollment is not None:
    # handle response
    pass
```
<!-- End SDK Example Usage [usage] -->