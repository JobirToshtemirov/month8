from aiogram.fsm.context import FSMContext
from aiogram import types, Router

from databases.database import database
from main.models import orders
from utils.basket import get_user_basket, clear_user_basket
from utils.notify_devs import send_notification_to_devs

router = Router()


@router.callback_query_handler(lambda c: c.data == "confirm_order")
async def confirm_order(callback_query: types.CallbackQuery, state: FSMContext):
    user_basket = await get_user_basket(callback_query.from_user.id)

    if user_basket:
        total_price = 0
        meal_ids = []

        for item in user_basket:
            meal_id = item['meal_id']
            quantity = item['quantity']
            price = item['price']
            meal_total = quantity * price
            total_price += meal_total
            meal_ids.append(meal_id)

        order_query = orders.insert().values(
            user_id=callback_query.from_user.id,
            total_price=total_price,
            meal_ids=meal_ids,
        )
        order_id = await database.execute(order_query)

        await callback_query.message.answer(f"Sizning buyurtmangiz tayor!  Jami: {total_price}. Raxmat!")

        await send_notification_to_devs(callback_query.message,
                                        f"Yangi buyurtma egasi {callback_query.from_user.id}. Jami: {total_price}")

        await clear_user_basket(callback_query.from_user.id)

    else:
        await callback_query.message.answer("Sizning qutingiz bosh biron nima qoshing.")
