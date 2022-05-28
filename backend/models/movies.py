from typing import Optional

from sqlmodel import SQLModel, Field


class Movies(SQLModel, table=True):

    __tablename__ = "movies"

    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    year: int
