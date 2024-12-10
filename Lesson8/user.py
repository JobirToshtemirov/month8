from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from . import schemas, crud
from .database import get_db
from .app import get_current_user

router = APIRouter()


# CRUD operations for the current user
@router.get("/users/me", response_model=schemas.User)
def get_current_user_data(current_user: schemas.User = Depends(get_current_user)):
    return current_user


@router.put("/users/me", response_model=schemas.User)
def update_current_user(
        user: schemas.UserUpdate,
        db: Session = Depends(get_db),
        current_user: schemas.User = Depends(get_current_user)
):
    return crud.update_user(db=db, user_id=current_user.id, user=user)


@router.delete("/users/me", response_model=dict)
def delete_current_user(
        db: Session = Depends(get_db),
        current_user: schemas.User = Depends(get_current_user)
):
    crud.delete_user(db=db, user_id=current_user.id)
    return {"detail": "Your account has been deleted"}


# Change password
@router.put("/users/change/password", response_model=dict)
def change_password(
        password_change: schemas.PasswordChange,
        db: Session = Depends(get_db),
        current_user: schemas.User = Depends(get_current_user)
):
    user = crud.get_user(db=db, user_id=current_user.id)
    if not user or not crud.verify_password(password_change.old_password, user.password):
        raise HTTPException(status_code=400, detail="Incorrect old password")
    crud.update_password(db=db, user_id=current_user.id, new_password=password_change.new_password)
    return {"detail": "Password updated successfully"}
