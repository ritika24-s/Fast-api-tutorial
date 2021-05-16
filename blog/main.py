#import
from fastapi import FastAPI
from . import models
from .database import engine
from .routers import blog, user, authentication


# creating the database
models.Base.metadata.create_all(bind=engine)


# initialize app
app = FastAPI()

# intialise routers
app.include_router(blog.router)
app.include_router(user.router)
app.include_router(authentication.router)