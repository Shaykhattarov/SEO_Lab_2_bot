from loader import bot, dp
from config import subjects_names
from aiogram import executor, types

from keyboards.inline.start_work import add_start_keyboard
from keyboards.inline.selection_menu import add_selection_menu
from keyboards.inline.answer_options import add_answer_options
from states.quest import get_subjects_with_quests


@dp.message_handler(commands='start')
async def start_message(message: types.Message):
    start_kb = add_start_keyboard()
    await message.answer(text="Привет :)", reply_markup=start_kb)


@dp.callback_query_handler(lambda c: c.data == 'start_work')
async def choose_subject(call: types.CallbackQuery):
    await bot.answer_callback_query(call.id)
    choice_keyboard = add_selection_menu(subjects_names, call_back_data="subjects")
    message_text = "Выбери предмет по которому хочешь пройти тест:"
    await bot.send_message(call.from_user.id, text=message_text, reply_markup=choice_keyboard)


@dp.callback_query_handler(lambda c: c.data == f'subjects')
async def send_question(call: types.CallbackQuery):
    await bot.answer_callback_query(call.id)
    print(call.values)


if __name__ == "__main__":
    subjects = get_subjects_with_quests()
    executor.start_polling(dp, skip_updates=True)

