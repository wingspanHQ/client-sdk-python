"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import serviceenablementresponse as shared_serviceenablementresponse
from ...models.shared import serviceenablementupdate as shared_serviceenablementupdate
from typing import Optional


@dataclasses.dataclass
class PatchBenefitsServiceIDRequest:
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    r"""Unique identifier"""
    service_enablement_update: Optional[shared_serviceenablementupdate.ServiceEnablementUpdate] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    



@dataclasses.dataclass
class PatchBenefitsServiceIDResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    service_enablement_response: Optional[shared_serviceenablementresponse.ServiceEnablementResponse] = dataclasses.field(default=None)
    r"""Indicates status of service enablement"""
    

