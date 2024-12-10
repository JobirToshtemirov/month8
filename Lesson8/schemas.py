from pydantic import BaseModel


class UserUpdate(BaseModel):
    email: str | None = None
    password: str | None = None


class PasswordChange(BaseModel):
    old_password: str
    new_password: str
