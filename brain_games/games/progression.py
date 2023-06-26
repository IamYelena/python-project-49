
from random import randint
TASK = 'What number is missing in the progression?'


MIN_NUMBER = 1
MAX_NUMBER = 10


def generate_progression(start_number, step):
    array = []
    for number in range(MIN_NUMBER - 1, MAX_NUMBER):
        element = + number * step
        array.append(element)
    return array


def get_progression_string(array):
    query_string = ''
    for element in array:
        query_string = query_string + str(element) + ' '
    query_string = query_string.strip()
    return query_string


def generate_question():
    start_number = randint(MIN_NUMBER, MAX_NUMBER)
    step = randint(MIN_NUMBER, MAX_NUMBER)
    number_hidden_element = randint(MIN_NUMBER - 1, MAX_NUMBER - 1)
    array = generate_progression(start_number, step)
    hidden_element = array[number_hidden_element]
    right_answer = hidden_element
    array[number_hidden_element] = '..'
    progression_string = get_progression_string(array)
    question_string = f': {progression_string}'
    return (question_string, right_answer)
