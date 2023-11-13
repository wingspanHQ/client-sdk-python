# SDK


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
import sdk
from sdk.models import operations

s = sdk.SDK()


res = s.get_benefits_enrollment_id_(id='string')

if res.enrollment is not None:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | Unique identifier  |


### Response

**[operations.GetBenefitsEnrollmentIDResponse](../../models/operations/getbenefitsenrollmentidresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## get_benefits_plan_enrollment

List all plan enrollments

### Example Usage

```python
import sdk

s = sdk.SDK()


res = s.get_benefits_plan_enrollment()

if res.classes is not None:
    # handle response
    pass
```


### Response

**[operations.GetBenefitsPlanEnrollmentResponse](../../models/operations/getbenefitsplanenrollmentresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## get_benefits_plan_enrollment_id_

Get a particular plan enrollment by ID

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK()


res = s.get_benefits_plan_enrollment_id_(id='string')

if res.plan_enrollment is not None:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *str*              | :heavy_check_mark: | Unique identifier  |


### Response

**[operations.GetBenefitsPlanEnrollmentIDResponse](../../models/operations/getbenefitsplanenrollmentidresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## get_benefits_service

Fetches the current status indicating whether the benefits service is enabled or disabled.

### Example Usage

```python
import sdk

s = sdk.SDK()


res = s.get_benefits_service()

if res.service_enablement_response is not None:
    # handle response
    pass
```


### Response

**[operations.GetBenefitsServiceResponse](../../models/operations/getbenefitsserviceresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## patch_benefits_service_id_

Allows users to change the enablement status of a specified benefits service.

### Example Usage

```python
import sdk
from sdk.models import operations, shared

s = sdk.SDK()


res = s.patch_benefits_service_id_(id='string', service_enablement_update=shared.ServiceEnablementUpdate(
    enabled=False,
))

if res.service_enablement_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `id`                                                                                       | *str*                                                                                      | :heavy_check_mark:                                                                         | Unique identifier                                                                          |
| `service_enablement_update`                                                                | [Optional[shared.ServiceEnablementUpdate]](../../models/shared/serviceenablementupdate.md) | :heavy_minus_sign:                                                                         | N/A                                                                                        |


### Response

**[operations.PatchBenefitsServiceIDResponse](../../models/operations/patchbenefitsserviceidresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |
