from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def add_answer_options(answer_options) -> InlineKeyboardMarkup:
    """ Создание клавиатуры с вариантами ответов на вопрос """

    answer_options_kb = InlineKeyboardMarkup()
    for num, option in enumerate(answer_options):
        button = InlineKeyboardButton(option, callback_data=f'option_{num}')
        answer_options_kb.add(button)
    return answer_options_kb


