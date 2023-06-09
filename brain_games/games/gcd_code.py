import prompt
from random import randint
import math
from brain_games.engine.command import proccessing_result


QUESTIONS_COUNT = 3
TASK = "Find the greatest common divisor of given numbers."
MIN_NUMBER = 1
MAX_NUMBER = 100


def generate_questions():
    print(TASK)
    res = run_game(QUESTIONS_COUNT, generate_question)
    return res


def generate_question():
    int1 = randint(MIN_NUMBER, MAX_NUMBER)
    int2 = randint(MIN_NUMBER, MAX_NUMBER)
    print(f'Question: {int1} {int2}')
    user_answer = prompt.string("Your answer:  ")
    right_answer = math.gcd(int1, int2)
    result = proccessing_result(user_answer, right_answer)
    return result
