# Benefits SDK


## Overview

Wingspan Benefits API: Benefits

### Available Operations

* [get_benefits_enrollment_id_](#get_benefits_enrollment_id_) - Retrieve Enrollment Details for a Specific Member
* [get_benefits_plan_enrollment](#get_benefits_plan_enrollment) - List all plan enrollments
* [get_benefits_plan_enrollment_id_](#get_benefits_plan_enrollment_id_) - Get a particular plan enrollment by ID
* [get_benefits_service](#get_benefits_service) - Retrieve Current Benefits Service Status
* [patch_benefits_service_id_](#patch_benefits_service_id_) - Modify Benefits Service Status

## get_benefits_enrollment_id_

Fetches the enrollment status and details for a member identified by the provided unique identifier.

### Example Usage

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

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.GetBenefitsEnrollmentIDRequest](../../models/operations/getbenefitsenrollmentidrequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |


### Response

**[operations.GetBenefitsEnrollmentIDResponse](../../models/operations/getbenefitsenrollmentidresponse.md)**


## get_benefits_plan_enrollment

List all plan enrollments

### Example Usage

```python
import benefits


s = benefits.Benefits()


res = s.benefits.get_benefits_plan_enrollment()

if res.plan_enrollments is not None:
    # handle response
    pass
```


### Response

**[operations.GetBenefitsPlanEnrollmentResponse](../../models/operations/getbenefitsplanenrollmentresponse.md)**


## get_benefits_plan_enrollment_id_

Get a particular plan enrollment by ID

### Example Usage

```python
import benefits
from benefits.models import operations

s = benefits.Benefits()

req = operations.GetBenefitsPlanEnrollmentIDRequest(
    id='<ID>',
)

res = s.benefits.get_benefits_plan_enrollment_id_(req)

if res.plan_enrollment is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                      | Type                                                                                                           | Required                                                                                                       | Description                                                                                                    |
| -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                      | [operations.GetBenefitsPlanEnrollmentIDRequest](../../models/operations/getbenefitsplanenrollmentidrequest.md) | :heavy_check_mark:                                                                                             | The request object to use for the request.                                                                     |


### Response

**[operations.GetBenefitsPlanEnrollmentIDResponse](../../models/operations/getbenefitsplanenrollmentidresponse.md)**


## get_benefits_service

Fetches the current status indicating whether the benefits service is enabled or disabled.

### Example Usage

```python
import benefits


s = benefits.Benefits()


res = s.benefits.get_benefits_service()

if res.service_enablement_response is not None:
    # handle response
    pass
```


### Response

**[operations.GetBenefitsServiceResponse](../../models/operations/getbenefitsserviceresponse.md)**


## patch_benefits_service_id_

Allows users to change the enablement status of a specified benefits service.

### Example Usage

```python
import benefits
from benefits.models import operations, shared

s = benefits.Benefits()

req = operations.PatchBenefitsServiceIDRequest(
    service_enablement_update=shared.ServiceEnablementUpdate(
        enabled=False,
    ),
    id='<ID>',
)

res = s.benefits.patch_benefits_service_id_(req)

if res.service_enablement_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.PatchBenefitsServiceIDRequest](../../models/operations/patchbenefitsserviceidrequest.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |


### Response

**[operations.PatchBenefitsServiceIDResponse](../../models/operations/patchbenefitsserviceidresponse.md)**

