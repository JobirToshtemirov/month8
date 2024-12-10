from pydantic import BaseModel
from typing import List, Optional

class NoteBase(BaseModel):
    title: str
    content: Optional[str]

class NoteCreate(NoteBase):
    pass

class Note(NoteBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True

class UserBase(BaseModel):
    name: str
    email: str

class UserCreate(UserBase):
    pass

class User(UserBase):
    id: int
    notes: List[Note] = []

    class Config:
        orm_mode = True
