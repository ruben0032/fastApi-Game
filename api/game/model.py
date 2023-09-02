from typing import Optional

from sqlmodel import Field, SQLModel

class Game(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    description: str
    studio: str
    publicDate: str
    urlImage: str
    
    publisherId: Optional[str] = Field(default=None, foreign_key="publisher.id")