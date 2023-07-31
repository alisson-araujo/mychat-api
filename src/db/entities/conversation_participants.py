from sqlmodel import SQLModel, Field
from typing import Optional
from .conversation import Conversations
from .user import Users


class CvsParticipants(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    conversation_id: int = Field(foreign_key=Conversations.id)
    user_id: int = Field(foreign_key=Users.id)
