from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder

from config.db import conn
from models.user import users
from schemas.user import User, LoginItem

user = APIRouter()

dummy_user = {
    "email": "dirreno@unal.edu.co",
    "password": "12345678"
}


@user.get("/users", response_model=list[User])
def get_users():
    return conn.execute(users.select()).fetchall()


@user.post("/users", response_model=User)
def create_user(user: User):
    created_user = {"name": user.name,
                    "email": user.email,
                    "password": user.password,
                    "position": user.position,
                    "skills": user.skills}
    n_user = conn.execute(users.insert().values(created_user))
    return n_user


@user.get("/users/{id}", response_model=User)
def get_user(id: str):
    data = conn.execute(users.select().where(users.c.id == id)).first()
    return data


@user.delete("/users/{id}")
def delete_user(id: str):
    conn.execute(users.delete().where(users.c.id == id)).first()
    return {"message": "Deleted user"}


@user.put("/users/{id}")
def update_user(id: str, user: User):
    conn.execute(users.update().values(name=user.name,
                                       email=user.email,
                                       password=user.password,
                                       position=user.position,
                                       skills=user.skills).where(users.c.id == id))
    return {"message": "Updated user"}


@user.get("/home")
async def root():
    return {"message": "Landing page"}


@user.post("/login")
def login(logged_data: LoginItem):
    logged_user = conn.execute(users.select().where(users.c.email == logged_data.email)).first()

    if logged_user is not None:
        if logged_data.password == logged_user.password:
            return logged_user
        else:
            return {"message": "Wrong password"}
    else:
        return {"message": "Wrong email"}