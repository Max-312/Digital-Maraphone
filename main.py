from fastapi import FastAPI, HTTPException
from .database import database
from .crud import get_user, create_user

app = FastAPI()

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

@app.get("/users/{user_id}")
async def read_user(user_id: int):
    user = await get_user(user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@app.post("/users/")
async def create_new_user(name: str, email: str):
    user_id = await create_user(name, email)
    return {"id": user_id, "name": name, "email": email}
