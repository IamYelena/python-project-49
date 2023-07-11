
from random import randint
TASK = 'What number is missing in the progression?'


MIN_NUMBER = 1
MAX_NUMBER = 10
MIN_STEP = 1
MAX_STEP = 10


def generate_progression(start_number, step):
    progression = []
    for number in range(MIN_NUMBER - 1, MAX_NUMBER):
        element = + number * step
        progression.append(element)
    return progression


def get_progression_string(progression):
    query_string = ''
    for element in progression:
        query_string = f"{query_string}{element} "
    query_string = query_string.strip()
    return query_string


def generate_question():
    start_number = randint(MIN_NUMBER, MAX_NUMBER)
    step = randint(MIN_STEP, MAX_STEP)
    hidden_element_index = randint(MIN_NUMBER - 1, MAX_NUMBER - 1)
    progression = generate_progression(start_number, step)
    hidden_element = progression[hidden_element_index]
    right_answer = hidden_element
    progression[hidden_element_index] = '..'
    progression_string = get_progression_string(progression)
    question_string = f'{progression_string}'
    return (question_string, right_answer)
