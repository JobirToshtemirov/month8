from aiogram.utils import executor
import handlers, middlewares, filters
from databaes.database import database
from utils.set_bot_commands import set_default_commands
from utils.notify_devs import send_notification_to_devs
from loader import dp


async def on_startup(dispatcher):
    await database.connect()
    await set_default_commands(dispatcher)

    await send_notification_to_devs(dispatcher)


async def on_shutdown(dispatcher):
    await database.disconnect()

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=False, on_shutdown=on_shutdown)
