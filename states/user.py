from aiogram.dispatcher.filters.state import StatesGroup, State


class UserData(StatesGroup):
    name = State()
    group = State()

