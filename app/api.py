from fastapi import FastAPI, Body, Depends

from app.models import PostSchema, UserLoginSchema, UserSchema
from app.auth.auth_bearer import JWTBearer
from app.auth.auth_handler import signJWT

#Posts array
posts = [
    {
        "id":1, 
        "title": "Baking",
        "content": "How to bake a red velvet cake"
    }
]

#Users array
users = []

app = FastAPI()

@app.get("/", tags=["root"])
async def root()-> dict:
    return {"message": "welcome to FastAPI JWT Auth"}


@app.get("/posts", tags=["posts"])
async def get_posts() -> dict:
    return {"data": posts}


@app.get("/posts/{id}", tags=["posts"])
async def get_single_post(id: int) -> dict:
    if id >len(posts) or id == 0:
        return {"data": "No such post with the suplied ID"}


    for post in posts:
        if post["id"] == id:
            return {"data": post}


@app.post("/posts",  dependencies=[Depends(JWTBearer())], tags=["posts"])
async def add_post(post: PostSchema) -> dict:
    post.id = len(posts) + 1
    posts.append(post.dict())
    return {"data": "post added"}


@app.post("/user/signup", tags=["user"])
async def create_user(user: UserSchema = Body(...)):
    users.append(user)
    return signJWT(user.email)


def check_user(data: UserLoginSchema):
    for user in users:
        if user.email == data.email and user.password == data.password:
            return True
    return False


@app.post("/user/login", tags=["user"])
async def user_login(user: UserLoginSchema = Body(...)):
    if check_user(user):
        return signJWT(user)
    return {
        "error": "Wrong Login Credentials"
    }




