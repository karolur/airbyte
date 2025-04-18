# generated by datamodel-codegen:
#   filename:  RolloutConfiguration.yaml

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Extra, Field, conint


class RolloutConfiguration(BaseModel):
    class Config:
        extra = Extra.forbid

    enableProgressiveRollout: Optional[bool] = Field(
        False, description="Whether to enable progressive rollout for the connector."
    )
    initialPercentage: Optional[conint(ge=0, le=100)] = Field(
        0,
        description="The percentage of users that should receive the new version initially.",
    )
    maxPercentage: Optional[conint(ge=0, le=100)] = Field(
        50,
        description="The percentage of users who should receive the release candidate during the test phase before full rollout.",
    )
    advanceDelayMinutes: Optional[conint(ge=10)] = Field(
        10,
        description="The number of minutes to wait before advancing the rollout percentage.",
    )
