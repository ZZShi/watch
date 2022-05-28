from typing import Optional

from sqlmodel import SQLModel, Field


class Users(SQLModel, table=True):

    __tablename__ = "users"

    id: Optional[int] = Field(default=None, primary_key=True)
    username: str
    password: str
    nickname: str
