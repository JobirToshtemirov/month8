from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils import executor

BOT_TOKEN = "7636239509:AAGoBxg02d2SmBnpRxJfCnmnemc1FLk7tnw"
ADMIN_ID = 6570388834

bot = Bot(BOT_TOKEN, parse_mode=types.ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

keyboard = ReplyKeyboardMarkup(
    resize_keyboard=True
).add(
    KeyboardButton(text="🍴 Меню")
).row(
    KeyboardButton(text="🛍 Мои заказы"),
).add(
    KeyboardButton(text="✍️ Оставить отзыв"),
    KeyboardButton(text="⚙️ Настройки")
)


class UserStates(StatesGroup):
    get_message = State()


@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    await message.answer(
        text=f"<b>Assalomu alaykum hurmatli {message.from_user.full_name}, botga hush kelibsiz!</b>",
        reply_markup=keyboard
    )


@dp.message_handler(text=["🍴 Меню"])
async def menyu(message: types.Message):
    await message.answer("Bizda hozircha menyu shakillangani yo'q. Tayyor bo'lishi bilan xabar beramiz!")



@dp.message_handler(text=["🛍 Мои заказы"])
async def zakazlar(message: types.Message):
    await message.answer("Bot hali ishga tushmagan. Zakaz qilish uchun ishga tushishini kuting.")


@dp.message_handler(text=["✍️ Оставить отзыв"])
async def handle_user_message(message: types.Message, state: FSMContext):
    await message.answer("Habaringizni kiriting: 👇")
    await state.set_state(UserStates.get_message.state)


@dp.message_handler(state=UserStates.get_message, content_types=types.ContentType.TEXT)
async def get_message(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    full_name = message.from_user.full_name
    username = message.from_user.username or "Не указан"
    text = message.text

    admin_text = (
        f"User ID: {user_id}\n"
        f"Username: {full_name} (@{username})\n"
        f"Premium: {message.from_user.is_premium}\n"
        f"Bot: {message.from_user.is_bot}\n"
        f"Foydalanuvchi matni:\n{text}"
    )
    await bot.send_message(chat_id=ADMIN_ID, text=admin_text)

    await message.reply("Sizning xabaringiz yuborildi. Admin javobini kuting!")
    await state.finish()


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=False)
