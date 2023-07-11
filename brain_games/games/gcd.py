from random import randint
import math

TASK = 'Find the greatest common divisor of given numbers.'
MIN_NUMBER = 1
MAX_NUMBER = 100


def generate_question():
    number1 = randint(MIN_NUMBER, MAX_NUMBER)
    number2 = randint(MIN_NUMBER, MAX_NUMBER)
    question_string = f'{number1} {number2}'
    right_answer = math.gcd(number1, number2)
    return (question_string, right_answer)
