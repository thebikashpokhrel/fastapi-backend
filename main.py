from fastapi import FastAPI, HTTPException
from enum import Enum

app = FastAPI()


class GenderURLChoices(Enum):
    MALE = "male"
    FEMALE = "female"


USERS = [
    {"id": 1, "name": "Jon Doe", "gender": "male"},
    {"id": 2, "name": "Andrew Ng", "gender": "male"},
    {"id": 3, "name": "Hitesh Choudhary", "gender": "male"},
    {"id": 4, "name": "Lily", "gender": "female"},
    {"id": 5, "name": "Olivia", "gender": "Female"},
]


@app.get("/users")
async def users() -> list[dict]:
    return USERS


@app.get("/user/{userId}")
async def user(userId: int) -> dict:
    user = None
    for u in USERS:
        if u["id"] == userId:
            user = u

    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@app.get("/user/gender/{gender}")
async def userByGender(gender: GenderURLChoices) -> list[dict]:
    return [user for user in USERS if user["gender"].lower() == gender.value]
