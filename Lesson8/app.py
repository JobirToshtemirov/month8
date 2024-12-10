from fastapi import FastAPI
from . import admin, user

app = FastAPI()

app.include_router(admin.router, prefix="/admin", tags=["admin"])
app.include_router(user.router, prefix="/user", tags=["user"])
