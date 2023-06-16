
from random import randint

MIN_NUMBER = 0
MAX_NUMBER = 100


def generate_question():
    v = randint(MIN_NUMBER, MAX_NUMBER)
    question_string = f'Question: {v}'
    right_answer = ''
    if v % 2 == 0:
        right_answer = 'yes'
    if v % 2 != 0:
        right_answer = 'no'
    return (question_string, right_answer)
