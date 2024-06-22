from datetime import date
from enum import Enum
from pydantic import BaseModel


class GenreURLChoices(Enum):
    SCIFI = "scifi"
    FANTASY = "fantasy"
    MYSTERY = "mystery"
    BIOGRAPHT = "biography"


class Post(BaseModel):
    id: int
    title: str
    created: date


class User(BaseModel):
    id: int
    name: str
    genre: str
    posts: list[Post] = []
