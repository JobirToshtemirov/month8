from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardButton, Message

BOT_TOKEN = "7633768347:AAEM-5CTvOkfNW2aVUttenGPVAQ8lXlIbmc"
ADMIN_ID = 6570388834

bot = Bot(BOT_TOKEN, parse_mode=types.ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    await message.answer(text="Salom Shef pastdagi tugmalardan birini tanlang", reply_markup=keyboard)


@dp.message_handler(text=["Salom✌️"])
async def salom(message: types.Message):
    await message.answer(text=f"<b>Assalomu alaykum hurmatli {message.from_user.full_name}  botga hush kelibsiz </b>")


@dp.message_handler(text=["Hayr🖖"])
async def hayr(message: types.Message):
    await message.answer(text="Hop sizgaham hayr")


@dp.message_handler(text=["Yo'qol😤"])
async def yoqol(message: types.Message):
    await message.answer(text=f"O'zing yo'qol  {message.from_user.full_name}")


@dp.message_handler(text='Adminga Murojat📩')
async def handle_user_message(message: types.Message, state: None):
    text = "Habaringizni kiriting: 👇"
    await message.answer(text)
    await bot.send_message(ADMIN_ID,
                           f"{message.from_user.full_name} (@{message.from_user.username}) dan:\n{message.text}")
    await dp.current_state(user=message.from_user.id).set_state('get_message')


@dp.message_handler(state='get_message', content_types=types.ContentType.TEXT)
async def get_message(message: types.Message, state: FSMContext):
    text = message.text
    text=f"User ID: {message.from_user.id}\nUsername: {message.from_user.full_name}\nPremium: {message.from_user.is_premium}\nFoydalanuvchi matni:\n {text} "
    user_id = ADMIN_ID
    await bot.send_message(
        chat_id=user_id,
        text=text,
        reply_markup=keyboard
    )
    await message.reply("\nSizning xabaringiz yuborildi \nAdmin javobini kuting !")
    await state.update_data(user_id=message.from_user.id)
    await state.finish()


@dp.message_handler(lambda message: message.chat.id == ADMIN_ID)
async def handle_admin_reply(message: Message):
    try:
        target_user_id = int(message.reply_to_message.forward_from.id)
        await bot.send_message(target_user_id, f"Admindan javob:\n{message.text}")
    except AttributeError:
        await message.reply("Hato")


keyboard = ReplyKeyboardMarkup(
    [
        [
            InlineKeyboardButton(text="Adminga Murojat📩")
        ],
        [
            InlineKeyboardButton(text="Salom✌️"),
            InlineKeyboardButton(text="Hayr🖖"),
        ],
        [
            InlineKeyboardButton(text="Yo'qol😤"),
        ]
    ],
    resize_keyboard=True
)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
