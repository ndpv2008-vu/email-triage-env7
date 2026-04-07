from pydantic import BaseModel
from typing import Optional, List


class Email(BaseModel):
    email_id: str
    sender: str
    subject: str
    body: str


class Observation(BaseModel):
    email_id: str
    sender: str
    subject: str
    body: str
    history: List[str]
    last_action_error: Optional[str] = None


class Action(BaseModel):
    action_type: str  # classify / prioritize / reply
    value: str        # spam / important / low / etc


class StepResult(BaseModel):
    observation: Observation
    reward: float
    done: bool
    info: dict