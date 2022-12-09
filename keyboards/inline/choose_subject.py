from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def add_choice_subject(subjects: list):
    """ Генерация клавиатуры выбора желаемого предмета """
    subjects = InlineKeyboardMarkup()
    for num, option in enumerate(answer_options):
        button = InlineKeyboardButton(option, callback_data=f'option_{num}')
        answer_options_kb.add(button)
    return answer_options_kb