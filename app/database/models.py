from datetime import datetime
from pydantic import BaseModel, Json
from typing import Dict, Any


class User(BaseModel):
    id: int
    active_chat_id: int
    username: str
    full_name: str
    llm_model: str
    timestamp: datetime


class Chat(BaseModel):
    id: int
    user_id: int
    name: str
    timestamp: datetime


class Message(BaseModel):
    id: int
    chat_id: int
    content: Json[Dict[str, Any]]
    timestamp: datetime
