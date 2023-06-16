from random import randint
import math


QUESTIONS_COUNT = 3
TASK = 'Find the greatest common divisor of given numbers.'
MIN_NUMBER = 1
MAX_NUMBER = 100


def generate_question():
    number1 = randint(MIN_NUMBER, MAX_NUMBER)
    number2 = randint(MIN_NUMBER, MAX_NUMBER)
    question_string = f'Question: {number1} {number2}'
    right_answer = math.gcd(number1, number2)
    return (question_string, right_answer)
