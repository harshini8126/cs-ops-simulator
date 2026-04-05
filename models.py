from pydantic import BaseModel
from typing import List, Optional

class Email(BaseModel):
    id: str
    subject: str
    body: str
    customer_id: str
    urgency: int

class Observation(BaseModel):
    inbox: List[Email]
    processed: List[str]
    time_left: int
    satisfaction: float

class Action(BaseModel):
    email_id: str
    category: str
    priority: str
    decision: str
    reply: Optional[str]

class Reward(BaseModel):
    score: float
    reason: str