from app.database import engine, Base


from fastapi import FastAPI
from app.routers import users, notes

app = FastAPI()

app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(notes.router, prefix="/notes", tags=["notes"])


Base.metadata.create_all(bind=engine)
