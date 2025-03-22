from datetime import datetime
from pydantic import BaseModel, Json
from typing import Dict, Any, Optional


class User(BaseModel):
    id: int
    active_chat_id: int
    username: Optional[str]
    full_name: Optional[str]
    timestamp: Optional[datetime]


class Chat(BaseModel):
    id: int
    user_id: int
    name: str
    agent: str
    llm_model: Optional[str]
    online_model: bool
    timestamp: datetime


class Message(BaseModel):
    id: int
    chat_id: int
    content: Json[Dict[str, Any]]
    timestamp: datetime
