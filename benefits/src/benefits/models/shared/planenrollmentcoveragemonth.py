"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import a71f30be878693b235f8c5f1650be03c9920ca9821526545760476436104c9dc as shared_a71f30be878693b235f8c5f1650be03c9920ca9821526545760476436104c9dc
from benefits import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum

class PlanEnrollmentCoverageMonthFundingStatus(str, Enum):
    PENDING = 'Pending'
    COMPLETE = 'Complete'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PlanEnrollmentCoverageMonth:
    amount_charged: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('amountCharged') }})
    funding_status: PlanEnrollmentCoverageMonthFundingStatus = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('fundingStatus') }})
    internal: shared_a71f30be878693b235f8c5f1650be03c9920ca9821526545760476436104c9dc.A71f30be878693b235f8c5f1650be03c9920ca9821526545760476436104c9dc = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('internal') }})
    month: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('month') }})
    

