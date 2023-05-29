import prompt

from random import randint
from brain_games.engine.command import proccessing_result

COUNT_OF_QUESTION = 3
TASK = 'Answer "yes" if the number is even, otherwise answer "no".'
MIN_NUMBER = 0
MAX_NUMBER = 100


def generate_questions():
    print(TASK)
    for i in range(COUNT_OF_QUESTION):
        res1 = generate_question()
        if res1 is False:
            return False
    return True


def generate_question():
    v = randint(MIN_NUMBER, MAX_NUMBER)
    print(f"Question: {v}")
    user_answer = ''
    while user_answer == '':
        user_answer = prompt.string('Your answer:  ')

    right_answer = ''
    if v % 2 == 0:
        right_answer = 'yes'
    if v % 2 != 0:
        right_answer = 'no'
    result = proccessing_result(user_answer, right_answer)
    return result
