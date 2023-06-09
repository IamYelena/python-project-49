import prompt

from random import randint, choice
from brain_games.engine.command import proccessing_result,run_game

QUESTIONS_COUNT = 3
TASK = "What is the result of the expression?"
MIN_NUMBER = 1
MAX_NUMBER = 30


def generate_questions():
    print(TASK)
    res = run_game(QUESTIONS_COUNT, generate_question)
    return res


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
