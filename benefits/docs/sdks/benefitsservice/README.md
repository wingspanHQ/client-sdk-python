# BenefitsService
(*benefits_service*)

## Overview

Operations related to service management

### Available Operations

* [get_benefits_service](#get_benefits_service) - Retrieve Current Benefits Service Status
* [patch_benefits_service_id_](#patch_benefits_service_id_) - Modify Benefits Service Status

## get_benefits_service

Fetches the current status indicating whether the benefits service is enabled or disabled.

### Example Usage

```python
import sdk

s = sdk.SDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.benefits_service.get_benefits_service()

if res.service_enablement_response is not None:
    # handle response
    pass

```


### Response

**[operations.GetBenefitsServiceResponse](../../models/operations/getbenefitsserviceresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## patch_benefits_service_id_

Allows users to change the enablement status of a specified benefits service.

### Example Usage

```python
import sdk
from sdk.models import shared

s = sdk.SDK(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.benefits_service.patch_benefits_service_id_(id='<value>', service_enablement_update=shared.ServiceEnablementUpdate(
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
| errors.SDKError | 4x-5xx          | */*             |
