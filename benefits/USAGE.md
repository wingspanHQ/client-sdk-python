<!-- Start SDK Example Usage -->


```python
import benefits
from benefits.models import operations

s = benefits.Benefits()

req = operations.GetBenefitsEnrollmentIDRequest(
    id='<ID>',
)

res = s.benefits.get_benefits_enrollment_id_(req)

if res.enrollment is not None:
    # handle response
    pass
```
<!-- End SDK Example Usage -->