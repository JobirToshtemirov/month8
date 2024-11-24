from aiogram.dispatcher.filters.state import StatesGroup, State


class UserStates(StatesGroup):
    get_message = State()


class RegisterState(StatesGroup):
    language = State()
    full_name = State()
    phone_number = State()
