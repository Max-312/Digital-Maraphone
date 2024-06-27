from .database import database
from .models import users

async def get_user(user_id: int):
    query = users.select().where(users.c.id == user_id)
    return await database.fetch_one(query)

async def create_user(name: str, email: str):
    query = users.insert().values(name=name, email=email)
    return await database.execute(query)
