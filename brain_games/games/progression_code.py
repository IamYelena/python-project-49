import prompt

from random import randint
from brain_games.engine.command import proccessing_result

QUESTIONS_COUNT = 3
TASK = "What number is missing in the progression?"
MIN_NUMBER = 1
MAX_NUMBER = 10

def generate_questions():
    print(TASK)
    res = run_game(QUESTIONS_COUNT, generate_question)
    return res


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
    array[number_hidden_element] = ".."

    query_string = ""
    for element in array:
        query_string = query_string + str(element) + " "
    query_string = query_string.strip()
    print(f"Question: {query_string}")
    user_answer = ''
    while user_answer == '':
        user_answer = prompt.string('Your answer:  ')

    result = proccessing_result(user_answer, right_answer)
    return result
