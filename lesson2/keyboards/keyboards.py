from aiogram.utils.i18n import gettext as _
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


async def user_main_menu_keyboard_with_lang(language: str) -> ReplyKeyboardMarkup:
    markup = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text=_("Menu 🍕", locale=language))
            ],
            [
                KeyboardButton(text=_("My orders 📖", locale=language)),
                KeyboardButton(text=_("Our branches 🏚", locale=language)),
            ],
            [
                KeyboardButton(text=_("Contact ☎️", locale=language)),
                KeyboardButton(text=_("Settings ⚙️", locale=language)),
            ]
        ],
        resize_keyboard=True
    )
    return markup


async def user_main_menu_keyboard() -> ReplyKeyboardMarkup:
    markup = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text=_("Menu 🍕"))
            ],
            [
                KeyboardButton(text=_("My orders 📖")),
                KeyboardButton(text=_("Our branches 🏚")),
            ],
            [
                KeyboardButton(text=_("Contact ☎️")),
                KeyboardButton(text=_("Settings ⚙️")),
            ]
        ],
        resize_keyboard=True
    )
    return markup


languages = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text=_("O'zbekcha 🇺🇿")),
            KeyboardButton(text=_("Русский 🇷🇺")),
            KeyboardButton(text=_("English 🇺🇸")),
        ]
    ],
    resize_keyboard=True
)

settings_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text=_("Change Language 🌍")),
            KeyboardButton(text=_("Go Back 🔙")),
        ]
    ],
    resize_keyboard=True
)


async def phone_number_share_keyboard():
    markup = ReplyKeyboardMarkup(
        keyboard=[[
            KeyboardButton(text="Share phone number ☎️", request_contact=True)
        ]], resize_keyboard=True
    )
    return markup
