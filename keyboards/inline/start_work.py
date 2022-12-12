from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def add_start_keyboard():
    button = InlineKeyboardButton('Начнем работу', callback_data='start_work')
    start_work = InlineKeyboardMarkup().add(button)
    return start_work

