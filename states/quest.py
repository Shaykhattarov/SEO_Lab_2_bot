import json
from config import filename, subjects_names
from aiogram.dispatcher.filters.state import StatesGroup, State


class Quest(object):
    quest_id: int
    question: str
    answer_options: list
    true_answer: str

    def __init__(self, quest_id: int, question: str, answer_options: list, true_answer: str):
        self.quest_id = quest_id
        self.question = question
        self.answer_options = answer_options
        self.true_answer = true_answer


class QuestData(StatesGroup):
    subject = State()
    answers = State()
    user_choice = State()
    counter = State()


def read_file():
    with open(filename, 'r', encoding='utf-8') as file:
        data = json.loads(file.read())
    return data


def get_subjects_with_quests(data):
    subjects = dict()
    for subject in subjects_names:
        subjects[subject] = []
        for num, quest in enumerate(data[subject]):
            quest = Quest(num, quest["question"], quest["answer_options"], quest["true_answer"])
            subjects[subject].append(quest)
    return subjects




