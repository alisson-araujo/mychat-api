from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime


class Users(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str
    phone: str
    password: str
    created_at: datetime = Field(default_factory=datetime.utcnow)