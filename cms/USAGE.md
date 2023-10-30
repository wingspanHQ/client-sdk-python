<!-- Start SDK Example Usage -->


```python
import sdk
from sdk.models import operations

s = sdk.SDK()


res = s.sdk.get_benefits_enrollment_id_(id='string')

if res.enrollment is not None:
    # handle response
    pass
```
<!-- End SDK Example Usage -->