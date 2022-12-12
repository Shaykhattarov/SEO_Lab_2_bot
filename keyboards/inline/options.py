from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def add_answer_options_keyboard(options):
    keyboard = InlineKeyboardMarkup()
    for num, option in enumerate(options):
        button = InlineKeyboardButton(option, callback_data=f'answer_{num + 1}')
        keyboard.add(button)
    return keyboard

