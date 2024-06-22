from fastapi import FastAPI, HTTPException
from schemas import GenreURLChoices, User
from users import USERS

app = FastAPI()


@app.get("/users")
async def users(
    genre: GenreURLChoices | None = None, hasPosts: bool = False
) -> list[User]:

    users_list = [User(**u) for u in USERS]

    if genre:
        users_list = [u for u in users_list if u.genre.lower() == genre.value]

    if hasPosts:
        users_list = [u for u in users_list if len(u.posts) > 0]

    return users_list


@app.get("/user/{userId}")
async def user(userId: int) -> User:
    user = None
    for u in USERS:
        if u["id"] == userId:
            user = User(**u)

    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@app.get("/user/genre/{genre}")
async def userByGenre(genre: GenreURLChoices) -> list[dict]:
    return [user for user in USERS if user["genre"].lower() == genre.value]
