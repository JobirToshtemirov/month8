from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, schemas
from app.database import get_db

router = APIRouter()

@router.post("/{user_id}/notes", response_model=schemas.Note)
def create_note(user_id: int, note: schemas.NoteCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    return crud.create_note(db, note, user_id)

@router.get("/{user_id}/notes", response_model=list[schemas.Note])
def read_notes(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    return crud.get_notes(db, user_id)
