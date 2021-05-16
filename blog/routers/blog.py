# imports

from fastapi import APIRouter, Depends, status
from typing import List
from sqlalchemy.orm import Session
from .. import schemas, oauth2
from ..database import get_db
from ..repository import blog

# create router
router = APIRouter(
    prefix = '/blog',
    tags = ['blogs']
)

# create apis

@router.get('/', response_model=List[schemas.ShowBlog])
def all_blogs(db: Session=Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.get_all(db)


@router.get('/{id}', status_code=200, response_model=schemas.ShowBlog)
def get_blog(id: int, db:Session=Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.detail(id, db)


@router.post('/create', status_code=status.HTTP_201_CREATED)
def create(request:schemas.Blog, db: Session=Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.create(request, db)


@router.delete('/delete/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_blog(id: int, db:Session=Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.delete(id, db)


@router.put('/update/{id}', status_code=status.HTTP_202_ACCEPTED)
def update_blog(id: int, request: schemas.Blog, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.update(id, request, db)