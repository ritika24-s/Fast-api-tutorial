from pydantic import BaseModel
from typing import List, Optional

class BlogBase(BaseModel):
    title:str
    body:str


class Blog(BlogBase):
    class Config():
        orm_mode = True

        
class ShowUser(BaseModel):
    name:str
    email:str
    blogs: List[Blog] = []


class User(ShowUser):
    password:str

    class Config():
        orm_mode = True
    

class ShowBlog(Blog):
    creator: ShowUser
    class Config():
        orm_mode = True


class Login(BaseModel):
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[str] = None