from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

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
