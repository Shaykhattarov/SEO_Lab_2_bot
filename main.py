from loader import bot, dp
from config import subjects_names
from aiogram import executor, types

from aiogram.dispatcher import FSMContext
from keyboards.inline.selection_menu import add_selection_menu
from keyboards.inline.confirm import add_confirm_keyboard
from keyboards.inline.options import add_answer_options_keyboard
from states.quest import get_subjects_with_quests, QuestData, read_file


@dp.message_handler(commands=['start'])
async def start_message(message: types.Message, state: FSMContext):
    keyboard = add_confirm_keyboard("Начать работу", "start_work")
    await message.answer(text="Привет :)", reply_markup=keyboard)


@dp.callback_query_handler(lambda c: c.data == "start_work")
async def choose_subject(call: types.CallbackQuery, state: FSMContext):
    await bot.answer_callback_query(call.id)

    # Работа с FSMContext
    await state.update_data(answers=[])
    await state.update_data(counter=0)
    await state.set_state(QuestData.subject)

    # Создание клавиатуры
    choice_keyboard = add_selection_menu(subjects_names)
    message = "Выбери предмет по которому хочешь пройти тест:"

    # Вывод сообщения
    await bot.send_message(call.from_user.id, text=message, reply_markup=choice_keyboard)
    return


@dp.callback_query_handler(lambda c: c.data in subjects_names, state=QuestData.subject)
async def enter_begging_test(call: types.CallbackQuery, state: FSMContext):
    await bot.answer_callback_query(call.id)

    # Работа с FSMContext
    await state.update_data(subject=call.data)
    await state.set_state(QuestData.counter)

    # Создание клавиатуры с началом теста
    keyboard_confirm = add_confirm_keyboard("Начать тест", call_back_data='next_question')
    await bot.send_message(call.from_user.id, text=f"Вы выбрали предмет: {call.data}", reply_markup=keyboard_confirm)
    return


@dp.callback_query_handler(lambda c: c.data == 'next_question', state=QuestData.counter)
async def send_question(call: types.CallbackQuery, state: FSMContext):
    await bot.answer_callback_query(call.id)

    async with state.proxy() as data:
        subject = data['subject']
        counter = data['counter']

        if counter < len(subjects[subject]):
            question = subjects[subject][counter].question
            answer_options = subjects[subject][counter].answer_options

            # Создание клавиатуры с вариантами ответов на вопрос
            answer_option_kb = add_answer_options_keyboard(answer_options)

            # Отправка сообщения с клавиатурой
            await bot.send_message(call.from_user.id, text=question, reply_markup=answer_option_kb)
        else:
            confirm = add_confirm_keyboard("Посмотреть результаты", "check_results")
            text = "Вы успешно прошли тест, нажмите на кнопку, чтобы посмотреть свои результаты"
            await bot.send_message(call.from_user.id, text=text, reply_markup=confirm)

    await state.update_data(counter=(counter + 1))
    await state.set_state(QuestData.answers)
    return


@dp.callback_query_handler(lambda c: c.data.endswith('answer_1'), state=QuestData.answers)
async def first_answer_option(call: types.CallbackQuery, state: FSMContext):
    await bot.answer_callback_query(call.id)
    async with state.proxy() as data:
        answers = data['answers']
    button_value = call.values['message']['reply_markup']['inline_keyboard'][0][0]['text']
    answers.append(button_value)
    await state.update_data(answers=answers)

    text = f"Ваш ответ: \n{button_value}"
    keyboard = add_confirm_keyboard('Дальше ->', call_back_data='next_question')
    await bot.send_message(call.from_user.id, text=text, reply_markup=keyboard)

    await state.set_state(QuestData.counter)
    return


@dp.callback_query_handler(lambda c: c.data.endswith('answer_2'), state=QuestData.answers)
async def second_answer_option(call: types.CallbackQuery, state: FSMContext):
    await bot.answer_callback_query(call.id)
    async with state.proxy() as data:
        answers = data['answers']
    button_value = call.values['message']['reply_markup']['inline_keyboard'][1][0]['text']
    answers.append(button_value)
    await state.update_data(answers=answers)

    text = f"Ваш ответ: \n{button_value}"
    keyboard = add_confirm_keyboard('Дальше ->', call_back_data='next_question')
    await bot.send_message(call.from_user.id, text=text, reply_markup=keyboard)

    await state.set_state(QuestData.counter)
    return


@dp.callback_query_handler(lambda c: c.data.endswith('answer_3'), state=QuestData.answers)
async def third_answer_option(call: types.CallbackQuery, state: FSMContext):
    await bot.answer_callback_query(call.id)
    async with state.proxy() as data:
        answers = data['answers']
    button_value = call.values['message']['reply_markup']['inline_keyboard'][2][0]['text']
    answers.append(button_value)
    await state.update_data(answers=answers)

    text = f"Ваш ответ: \n{button_value}"
    keyboard = add_confirm_keyboard('Дальше ->', call_back_data='next_question')
    await bot.send_message(call.from_user.id, text=text, reply_markup=keyboard)

    await state.set_state(QuestData.counter)
    return


@dp.callback_query_handler(lambda c: c.data.endswith('answer_4'), state=QuestData.answers)
async def fourth_answer_option(call: types.CallbackQuery,  state: FSMContext):
    await bot.answer_callback_query(call.id)
    async with state.proxy() as data:
        answers = data['answers']
    button_value = call.values['message']['reply_markup']['inline_keyboard'][3][0]['text']
    answers.append(button_value)
    await state.update_data(answers=answers)

    text = f"Ваш ответ: \n{button_value}"
    keyboard = add_confirm_keyboard('Дальше ->', call_back_data='next_question')
    await bot.send_message(call.from_user.id, text=text, reply_markup=keyboard)
    await state.set_state(QuestData.counter)
    return


@dp.callback_query_handler(lambda c: c.data == 'check_results', state=QuestData.answers)
async def check_results(call: types.CallbackQuery, state: FSMContext):
    await bot.answer_callback_query(call.id)

    async with state.proxy() as data:
        subject = data['subject']
        answers = data['answers']
    text = "Ваши результаты: \n"
    for num, answer in enumerate(answers):
        if subjects[subject][num].true_answer == answer:
            text += f"{num + 1}. {answer} ✅\n"
        else:
            text += f"{num + 1}. {answer} ❌\n"
    keyboard = add_confirm_keyboard("Попробовать еще раз", 'start_work')
    await bot.send_message(call.from_user.id, text=text, reply_markup=keyboard)
    await state.finish()
    return


if __name__ == "__main__":
    subjects = get_subjects_with_quests(read_file())
    executor.start_polling(dp, skip_updates=True)

