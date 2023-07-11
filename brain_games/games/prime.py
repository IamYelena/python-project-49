
from random import randint
TASK = 'Answer "yes" if given number is prime. Otherwise answer "no".'


MAX_NUMBER = 100
MIN_NUMBER = 1


def is_prime(number):
    if number == 1 or number == 0:
        return False
    for i in range(2, number - 1):
        if (number % i == 0):
            return False
    return True


def generate_question():
    number = randint(MIN_NUMBER, MAX_NUMBER)
    right_answer = 'no'
    if is_prime(number):
        right_answer = 'yes'

    question_string = f'{number}'

    return (question_string, right_answer)
