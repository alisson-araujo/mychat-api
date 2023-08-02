from sqlmodel import SQLModel, Field
from typing import Optional
from .conversation import Conversation
from .user import User


class CvsParticipants(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    conversation_id: int = Field(foreign_key=Conversation.id)
    user_id: int = Field(foreign_key=User.id)
