from sqlmodel import SQLModel, Field
from typing import Optional


class Conversations(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    # user_id: int = Field(foreign_key="user.id")
    name: str
