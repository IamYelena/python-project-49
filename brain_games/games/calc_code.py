import prompt

from random import randint, choice
from brain_games.engine.command import proccessing_result

COUNT_OF_QUESTION = 3
TASK = "What is the result of the expression?"
MIN_NUMBER = 1
MAX_NUMBER = 30


def generate_questions():
    print("What is the result of the expression?")
    for i in range(COUNT_OF_QUESTION):
        res1 = generate_question()
        if res1 is False:
            return False
    return True


def generate_question():
    int1 = randint(MIN_NUMBER, MAX_NUMBER)
    int2 = randint(MIN_NUMBER, MAX_NUMBER)
    operator = choice(["+", "-", "*"])
    print(f'Question: {int1} {operator} {int2}')
    user_answer = prompt.string("Your answer:  ")
    if operator == "+":
        right_answer = int1 + int2

    if operator == "-":
        right_answer = int1 - int2

    if operator == "*":
        right_answer = int1 * int2
    result = proccessing_result(user_answer, right_answer)
    return result
