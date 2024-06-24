from fastapi import FastAPI, HTTPException, Path, Query, Depends
from models import GenreChoices, GenreURLChoices, UserCreate, User, Post
from users import USERS
from typing import Annotated
from sqlmodel import Session, select
from db import init_db, get_session


# Type annotation can be used to add extra meta data to the data type assigned


app = FastAPI()


@app.get("/users")
async def users(
    genre: GenreURLChoices | None = None,
    q: Annotated[str | None, Query(max_length=20)] = None,
    session: Session = Depends(get_session),
) -> list[User]:

    users_list = session.exec(select(User)).all()

    if genre:
        users_list = [u for u in users_list if u.genre.value.lower() == genre.value]

    if q:
        users_list = [u for u in users_list if q.lower() in u.name.lower()]

    return users_list


@app.get("/user/{userId}")
async def user(
    userId: Annotated[int, Path(title="The user id")],
    session: Session = Depends(get_session),
) -> User:
    user = session.get(User, userId)

    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@app.get("/user/genre/{genre}")
async def userByGenre(
    genre: GenreChoices,
    session: Session = Depends(get_session),
) -> list[User]:
    statement = select(User).where(User.genre == genre)
    users_list = session.exec(statement)
    return users_list


@app.post("/users")
async def createUser(
    user_data: UserCreate, session: Session = Depends(get_session)
) -> User:
    user = User(name=user_data.name, genre=user_data.genre)
    session.add(user)

    if user_data.posts:
        for post in user_data.posts:
            postObj = Post(title=post.title, created=post.created, user=user)

            session.add(postObj)

    session.commit()
    session.refresh(user)
    return user
