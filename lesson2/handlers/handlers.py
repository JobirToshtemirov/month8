from aiogram import types
from aiogram.dispatcher import FSMContext

from keyboards import keyboards
from keyboards.keyboards import keyboard
from loader import dp, bot
from main.config import ADMINS
from states.states import UserStates


@dp.message_handler(commands="start")
async def start_handler(message: types.Message):
    text = f"<b> Assalomu alaykum\t{message.from_user.full_name}\tTJ-food (test) botiga hush kelibsiz </b>"
    await message.answer(text=text, reply_markup=keyboard)


@dp.message_handler(text=["🍴 Меню"])
async def menyu(message: types.Message):
    await message.answer("Bizda hozircha menyu shakillangani yo'q. Tayyor bo'lishi bilan xabar beramiz!")


@dp.message_handler(text=["🛍 Мои заказы"])
async def zakazlar(message: types.Message):
    await message.answer("Bot hali ishga tushmagan. Zakaz qilish uchun ishga tushishini kuting.")


@dp.message_handler(text=["✍️ Оставить отзыв"])
async def handle_user_message(message: types.Message, state: FSMContext):
    await message.answer("Habaringizni kiriting: 👇")
    await UserStates.get_message.set()


@dp.message_handler(state=UserStates.get_message, content_types=types.ContentType.TEXT)
async def get_message(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    full_name = message.from_user.full_name or "Ismi korsatilmagan"
    username = message.from_user.username or "Korsatilamagan"
    text = message.text

    admin_text = (
        f"\t\t<b>User Info</b>\n"
        f"User ID: {user_id}\n"
        f"Username: {full_name} (@{username})\n"
        f"Premium: {message.from_user.is_premium}\n"
        f"Bot: {message.from_user.is_bot}\n"
        f"Foydalanuvchi matni:\n{text}"
    )
    await bot.send_message(chat_id=ADMINS, text=admin_text)

    await message.reply("Sizning xabaringiz yuborildi. Admin javobini kuting!")
    await state.finish()