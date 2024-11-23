from aiogram.utils import executor

from main.evos import dp

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
