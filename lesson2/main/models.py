import sqlalchemy
from sqlalchemy import DateTime, func

from main.constants import UserStatus
from databaes.database import metadata

users = sqlalchemy.Table(
    "users",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("username", sqlalchemy.String, nullable=True),
    sqlalchemy.Column("full_name", sqlalchemy.String, nullable=True),
    sqlalchemy.Column("language", sqlalchemy.String, nullable=True),
    sqlalchemy.Column("chat_id", sqlalchemy.BigInteger, unique=True, nullable=False),
    sqlalchemy.Column("phone_number", sqlalchemy.String, nullable=True),
    sqlalchemy.Column("status", sqlalchemy.String, default=UserStatus.active, nullable=False),
    sqlalchemy.Column('created_at', DateTime(timezone=True), server_default=func.now(), nullable=False),
    sqlalchemy.Column('updated_at', DateTime(timezone=True), onupdate=func.now(), nullable=False)
)