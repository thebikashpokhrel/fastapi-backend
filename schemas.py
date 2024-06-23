from datetime import date
from enum import Enum
from pydantic import BaseModel, field_validator


class GenreURLChoices(Enum):
    SCIFI = "scifi"
    FANTASY = "fantasy"
    MYSTERY = "mystery"
    BIOGRAPHY = "biography"


class GenreChoices(Enum):
    SCIFI = "scifi"
    FANTASY = "fantasy"
    MYSTERY = "mystery"
    BIOGRAPHY = "biography"


class Post(BaseModel):
    id: int
    title: str
    created: date


class UserBase(BaseModel):
    name: str
    genre: GenreChoices
    posts: list[Post] = []


class UserCreate(UserBase):
    @field_validator("genre", mode="before")
    @classmethod
    def titleCaseGenre(cls, value: str):
        return value.lower()


class UserWithId(UserBase):
    id: int
