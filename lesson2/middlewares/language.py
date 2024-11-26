
from aiogram import types, Dispatcher
from aiogram.i18n import I18n
from aiogram.types import TelegramObject

from main.config import I18N_DOMAIN, LOCALES_DIR
from utils.db_commands.user import get_user


async def get_lang(user_id: int) -> str:
    user = await get_user(user_id)
    return user["language"] if user else "en"


class ACLMiddleware:
    def __init__(self, i18n: I18n):
        self.i18n = i18n

    async def __call__(self, handler, event: TelegramObject, data: dict):
        if isinstance(event, types.Message):
            user_id = event.from_user.id
            locale = await get_lang(user_id)
            self.i18n.context.set_locale(locale)

        return await handler(event, data)


def setup_middleware(dp: Dispatcher) -> I18n:
    i18n = I18n(domain=I18N_DOMAIN, path=LOCALES_DIR)

    dp.update.middleware(ACLMiddleware(i18n))

    return i18n
