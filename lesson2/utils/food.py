from aiogram import types
from aiogram.types import InlineKeyboardButton,p
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram import Router
from databases.database import database
from main.models import meals

router = Router()


async def get_available_meals():
    query = meals.select().where(meals.c.available == True)
    result = await database.fetch_all(query)
    return result


async def show_meal_menu(message: types.Message):
    meals_list = await get_available_meals()
    builder = InlineKeyboardBuilder()

    for meal in meals_list:
        meal_name = meal["meal_name"]
        meal_id = meal["id"]
        price = meal["price"]

        button = InlineKeyboardButton(
            text=f"{meal_name} - ${price}",
            callback_data=f"order_{meal_id}"
        )
        builder.add(button)
    builder.adjust(2)

    await message.answer("Choose a meal to order:", reply_markup=builder.as_markup())
