from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
from .. import schemas, models, token
from ..database import get_db
from ..hashing import Hash

router = APIRouter(
    tags = ['authentication']
)


@router.post('login/')
def login(request:OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == request.username).first()

    if not user or not Hash.verify(request.password, user.password,):
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,
                            details = 'Invalid credentials')

    access_token = token.create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}