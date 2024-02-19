# BenefitsEnrollment
(*benefits_enrollment*)

## Overview

Operations related to enrollments

### Available Operations

* [get_benefits_enrollment_id_](#get_benefits_enrollment_id_) - Retrieve Enrollment Details for a Specific Member
* [get_benefits_plan_enrollment](#get_benefits_plan_enrollment) - List all plan enrollments
* [get_benefits_plan_enrollment_id_](#get_benefits_plan_enrollment_id_) - Get a particular plan enrollment by ID

## get_benefits_enrollment_id_

Fetches the enrollment status and details for a member identified by the provided unique identifier.

### Example Usage

```python
import sdk

s = sdk.SDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.benefits_enrollment.get_benefits_enrollment_id_(id='<value>')

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
| errors.SDKError | 4x-5xx          | */*             |

## get_benefits_plan_enrollment

List all plan enrollments

### Example Usage

```python
import sdk

s = sdk.SDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.benefits_enrollment.get_benefits_plan_enrollment()

if res.classes is not None:
    # handle response
    pass
```


### Response

**[operations.GetBenefitsPlanEnrollmentResponse](../../models/operations/getbenefitsplanenrollmentresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_benefits_plan_enrollment_id_

Get a particular plan enrollment by ID

### Example Usage

```python
import sdk

s = sdk.SDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.benefits_enrollment.get_benefits_plan_enrollment_id_(id='<value>')

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
| errors.SDKError | 4x-5xx          | */*             |
