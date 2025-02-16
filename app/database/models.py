from datetime import datetime
from pydantic import BaseModel


class User(BaseModel):
    id: int
    username: str
    full_name: str
    timestamp: datetime


class Chat(BaseModel):
    id: int
    user_id: int
    name: str
    timestamp: datetime


class Message(BaseModel):
    id: int
    chat_id: int
    content: dict
    timestamp: datetime
