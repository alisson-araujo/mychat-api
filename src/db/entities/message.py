from sqlmodel import SQLModel, Field
from .conversation import Conversations
from .user import Users
from typing import Optional
from datetime import datetime


class Messages(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    conversation_id: int = Field(foreign_key=Conversations.id)
    user_id: int = Field(foreign_key=Users.id)
    content: str
    sent_at: datetime = Field(default=datetime.now())
