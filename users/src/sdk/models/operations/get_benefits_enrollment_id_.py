"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import enrollment as shared_enrollment
from typing import Optional


@dataclasses.dataclass
class GetBenefitsEnrollmentIDRequest:
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    r"""Unique identifier"""
    



@dataclasses.dataclass
class GetBenefitsEnrollmentIDResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    enrollment: Optional[shared_enrollment.Enrollment] = dataclasses.field(default=None)
    r"""An Enrollment records"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    

