from aiogram import Router, types
from aiogram.filters import Text

from loader import _
from keyboards import settings_menu, user_main_menu_keyboard

router = Router()

@router.message(Text(text="Settings ⚙️"))
async def settings_handler(message: types.Message):
    await message.reply(text=_("Sozlamalar:"), reply_markup=settings_menu)


@router.message(Text(text="Change Language 🌍"))
async def change_language_handler(message: types.Message):
    await message.reply(text=_("Til sozlamalari:\n1️⃣ English\n2️⃣ Russain\n3️⃣ O'zbekcha"))


@router.message(Text(text="Orqaga 🔙"))
async def go_back_handler(message: types.Message):
    await message.reply(text=_("Bosh meyuga qaytish:"), reply_markup=user_main_menu_keyboard)