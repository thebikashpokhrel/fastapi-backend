from fastapi import FastAPI, HTTPException, Path, Query
from schemas import GenreURLChoices, UserBase, UserCreate, UserWithId
from users import USERS
from typing import Annotated

# Type annotation can be used to add extra meta data to the data type assigned

app = FastAPI()


@app.get("/users")
async def users(
    genre: GenreURLChoices | None = None,
    q: Annotated[str | None, Query(max_length=20)] = None,
) -> list[UserWithId]:

    users_list = [UserWithId(**u) for u in USERS]
    print(users_list)

    if genre:
        users_list = [u for u in users_list if u.genre.value.lower() == genre.value]

    if q:
        users_list = [u for u in users_list if q.lower() in u.name.lower()]

    return users_list


@app.get("/user/{userId}")
async def user(userId: Annotated[int, Path(title="The user id")]) -> UserWithId:
    user = None
    for u in USERS:
        if u["id"] == userId:
            user = UserWithId(**u)

    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@app.get("/user/genre/{genre}")
async def userByGenre(genre: GenreURLChoices) -> list[dict]:
    return [user for user in USERS if user["genre"].lower() == genre.value]


@app.post("/users")
async def createUser(user_data: UserCreate) -> UserWithId:
    id = USERS[-1]["id"] + 1
    user = UserWithId(id=id, **user_data.model_dump()).model_dump()
    USERS.append(user)
    return user
