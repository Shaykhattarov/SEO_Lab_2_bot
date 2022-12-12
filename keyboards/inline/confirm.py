from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def add_confirm_keyboard(option, call_back_data=None):
    """ Добавление одно кнопочной клавиатуры """
    keyboard = InlineKeyboardMarkup()
    if call_back_data is not None:
        button = InlineKeyboardButton(option, callback_data=call_back_data)
    else:
        button = InlineKeyboardButton(option, callback_data=f"{option}")
    keyboard.add(button)
    return keyboard

