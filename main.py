from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]

@app.get('/')
def index():
    return {'data':'blog list'}

@app.get('/blog/unpublished')
def unpublished():
    return {'data':'all unpublished blogs'}

@app.get('/blog/{id}')
def show(id: int):
    return {'data':id}

@app.get('/blog/{id}/comments')
def comments(id: int):
    comments = id.get(comments)
    return {'data':comments}

@app.post('/blog')
def create_blog(request: Blog):
    return {'data':id, 'status': 'success'}