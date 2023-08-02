from sqlmodel import SQLModel, Field
from .conversation import Conversation
from .user import User
from typing import Optional
from datetime import datetime


class Message(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    conversation_id: int = Field(foreign_key=Conversation.id)
    user_id: int = Field(foreign_key=User.id)
    content: str
    sent_at: datetime = Field(default=datetime.now())
