import prompt
from random import randint
import math
from brain_games.engine.command import proccessing_result


COUNT_OF_QUESTION = 3
TASK = "Find the greatest common divisor of given numbers."
MIN_NUMBER = 1
MAX_NUMBER = 100


def generate_questions():
    print(TASK)
    for i in range(COUNT_OF_QUESTION):
        res1 = generate_question()
        if res1 is False:
            return False
    return True


def generate_question():
    int1 = randint(MIN_NUMBER, MAX_NUMBER)
    int2 = randint(MIN_NUMBER, MAX_NUMBER)
    print(f'Question: {int1} {int2}')
    user_answer = prompt.string("Your answer:  ")
    right_answer = math.gcd(int1, int2)
    result = proccessing_result(user_answer, right_answer)
    return result
