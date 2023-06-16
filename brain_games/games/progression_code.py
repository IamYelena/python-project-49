
from random import randint


MIN_NUMBER = 1
MAX_NUMBER = 10


def generate_question():
    start_number = randint(MIN_NUMBER, MAX_NUMBER)
    step = randint(MIN_NUMBER, MAX_NUMBER)
    number_hidden_element = randint(MIN_NUMBER - 1, MAX_NUMBER - 1)
    array = []
    for number in range(MIN_NUMBER - 1, MAX_NUMBER):
        element = start_number + number * step
        array.append(element)

    hidden_element = array[number_hidden_element]
    right_answer = hidden_element
    array[number_hidden_element] = '..'

    query_string = ''
    for element in array:
        query_string = query_string + str(element) + ' '
    query_string = query_string.strip()
    question_string = f'Question: {query_string}'
    return (question_string, right_answer)
