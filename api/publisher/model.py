from typing import Optional

from sqlmodel import Field, SQLModel

class Publisher(SQLModel, table=True):
    id: Optional[str] = Field(default=None, primary_key=True)
    description: str