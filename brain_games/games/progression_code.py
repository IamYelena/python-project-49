import prompt

from random import randint
from brain_games.engine.command import proccessing_result

COUNT_OF_QUESTION = 3
TASK = "What number is missing in the progression?"


def generate_questions():
    print(TASK)
    for i in range(COUNT_OF_QUESTION):
        res1 = generate_question()
        if res1 is False:
            return False
    return True


def generate_question():
    start_number = randint(1, 10)
    step = randint(1, 10)
    number_hidden_element = randint(0, 9)
    array = []
    for number in range(0, 10):
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
