# imports
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import schemas, models
from ..database import get_db
from ..repository import user

# initialise router
router = APIRouter(
    prefix = '/user',
    tags = ['users']
)


# create apis
@router.post('/create', response_model=schemas.ShowUser)
def create_users(request: schemas.User, db: Session=Depends(get_db)):
    return user.create_user(request, db)


@router.get('/{id}', status_code=200, response_model=schemas.ShowUser)
def get_user(id: int, db: Session = Depends(get_db)):
    return user.show_user(id, db)