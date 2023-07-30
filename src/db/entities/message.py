from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime


class Messages(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    conversation_id: int = Field(foreign_key="conversations.id")
    user_id: int = Field(foreign_key="users.id")
    content: str
    sent_at: datetime = Field(default=datetime.now())
