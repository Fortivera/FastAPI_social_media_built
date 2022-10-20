from fastapi import APIRouter, Body, FastAPI, Response, status, HTTPException, Depends
from .. import models, schemas, utils, database, oauth2
from sqlalchemy.orm import Session
from ..database import get_db


router = APIRouter(tags=['Authentication'])


@router.post("/login")
def login(user_credentials: OAuth2PasswordRequestFrom, db: Session = Depends(database.get_db)):

    user = db.query(models.User).filter(
        models.User.email == user_credentials.email).first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Invalid credentials")

    if not utils.verify_user(user_credentials.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Invalid credentials")
    access_token = oauth2.create_access_token(data={'user_id': user.id})
    return {"access_token": access_token, "token_type": 'bearer'}
