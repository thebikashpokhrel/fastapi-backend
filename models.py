from datetime import date
from enum import Enum
from pydantic import BaseModel, field_validator
from sqlmodel import Field, SQLModel, Relationship


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


class PostBase(SQLModel):
    title: str
    created: date
    userId: int | None = Field(foreign_key="user.id")


class Post(PostBase, table=True):
    id: int = Field(default=None, primary_key=True)
    user: "User" = Relationship(back_populates="posts")

    # Backpopulate value is the name of attribute in the other model i.e. posts attribute in user model


class UserBase(SQLModel):
    name: str
    genre: GenreChoices


class UserCreate(UserBase):
    posts: list[PostBase] | None = None

    @field_validator("genre", mode="before")
    @classmethod
    def titleCaseGenre(cls, value: str):
        return value.lower()


class User(UserBase, table=True):
    id: int = Field(default=None, primary_key=True)
    posts: list[Post] = Relationship(back_populates="user")
