from aiogram import Router
from sqlalchemy import insert, delete, select

from databases.database import database
from main.models import orders, user_basket, meals

router = Router()


async def get_user_basket(user_id: int):
    query = select(user_basket).where(user_basket.user_id == user_id)
    result = await database.fetch_all(query)
    return result


async def add_meal_to_basket(user_id: int, meal_id: int, quantity: int):
    query = select([meals.c.price]).where(meals.c.id == meal_id)
    meal_price = await database.fetch_one(query)
    price = meal_price["price"] if meal_price else 0.0

    insert_query = insert(user_basket).values(
        user_id=user_id,
        meal_id=meal_id,
        quantity=quantity,
        price=price
    )
    await database.execute(insert_query)


async def remove_meal_from_basket(user_id: int, meal_id: int):
    delete_query = delete(user_basket).where(
        user_basket.c.user_id == user_id,
        user_basket.c.meal_id == meal_id
    )
    await database.execute(delete_query)


async def clear_user_basket(user_id: int):
    delete_query = delete(user_basket).where(user_basket.c.user_id == user_id)
    await database.execute(delete_query)


async def place_order(user_id: int, total_price: float, meal_ids: list):
    insert_query = insert(orders).values(
        user_id=user_id,
        total_price=total_price,
        meal_ids=meal_ids,
    )
    order_id = await database.execute(insert_query)
    return order_id
