from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "Startto use bot🚀"),
            types.BotCommand("help", "Find all features🤖"),
            types.BotCommand("Feedback", "Send feedback to admin📝"),

        ]
    )