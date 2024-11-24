from loader import bot
from main.config import DEVS

from loader import logger


async def send_notification_to_devs(dispatcher):
    try:
        for dev in DEVS:
            await bot.send_message(text="Bot started !", chat_id=dev)
    except Exception as e:
        logger.error(f"While sending info to devs: {e}")
