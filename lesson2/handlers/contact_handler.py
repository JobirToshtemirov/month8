from aiogram import Router, types
from aiogram.filters import Text
from loader import *

router = Router()


@router.message(Text(text=["Aloqa ☎️"]))
async def contact_handler(message: types.Message):
    text = _("📲 Call center: 1006 or 99-033-09-52")
    await message.answer(text=text)
