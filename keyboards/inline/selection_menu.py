from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def add_selection_menu(choices: list, call_back_data=None):
    """ Создание клавиатуры с вариантами ответов """
    selection_menu_kb = InlineKeyboardMarkup()
    for num, choice in enumerate(choices):
        if call_back_data:
            button = InlineKeyboardButton(choice, callback_data=call_back_data)
            selection_menu_kb.add(button)
        else:
            button = InlineKeyboardButton(choice, callback_data=f"{choice}")
            selection_menu_kb.add(button)
    return selection_menu_kb

