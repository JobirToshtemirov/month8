from typing import Union
from aiogram import types
# from logging_settings import logger
from databases.database import database
from loader import logger
from main.constants import UserStatus
from main.models import users


async def get_user(chat_id: int) -> Union[dict, None]:
    try:
        query = users.select().where(users.c.chat_id == chat_id)
        row = await database.fetch_one(query=query)
        return dict(row) if row else None
    except Exception as e:
        error_text = f"Error retrieving user with ID {chat_id}: {e}"
        logger.error(error_text)
        return None


async def add_user(message: types.Message, data: dict) -> Union[int, None]:
    try:
        query = users.insert().values(
            chat_id=message.chat.id,
            full_name=data.get("full_name"),
            phone_number=data.get("phone_number"),
            language=data.get('language'),
            username=message.from_user.username,
            status=UserStatus.active,
            created_at=message.date,
            updated_at=message.date
        ).returning(users.c.id)
        new_user_id = await database.execute(query=query)
        return new_user_id
    except Exception as e:
        error_text = f"Error adding new user{message.chat.id}: {e}"
        logger.error(error_text)
        return None