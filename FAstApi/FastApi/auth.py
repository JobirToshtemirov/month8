from fastapi import FastAPI
from . import auth
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from datetime import datetime, timedelta
import jwt
from . import schemas, crud

app = FastAPI()
app.include_router(auth.router, prefix="/auth", tags=["auth"])


# Config
SECRET_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIx"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Password hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Router
router = APIRouter()


# Utility functions
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)


def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)


# Register endpoint
@router.post("/register", response_model=schemas.Author)
def register(Author: schemas.AuthorCreate, db: Session = Depends(get_db)):
    db_Author = crud.get_Author_by_email(db, email=Author.email)
    if db_Author:
        raise HTTPException(status_code=400, detail="Email is already registered")
    hashed_password = get_password_hash(Author.password)
    Author.password = hashed_password
    return crud.create_Author(db=db, Author=Author)


# Login endpoint
@router.post("/login")
def login(Author: schemas.AuthorLogin, db: Session = Depends(get_db)):
    db_Author = crud.get_Author_by_email(db, email=Author.email)
    if not db_Author or not verify_password(Author.password, db_Author.password):
        raise HTTPException(status_code=401, detail="Invalid email or password")
    access_token = create_access_token(data={"sub": db_Author.email})
    return {"access_token": access_token, "token_type": "bearer"}
