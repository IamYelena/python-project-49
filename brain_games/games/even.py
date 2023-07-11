
from random import randint
TASK = 'Answer "yes" if the number is even, otherwise answer "no".'

MIN_NUMBER = 0
MAX_NUMBER = 100


def is_even(number):
    return number % 2 == 0


def generate_question():
    number = randint(MIN_NUMBER, MAX_NUMBER)
    question_string = f'{number}'
    right_answer = ''
    if is_even(number):
        right_answer = 'yes'
    else:
        right_answer = 'no'
    return (question_string, right_answer)
