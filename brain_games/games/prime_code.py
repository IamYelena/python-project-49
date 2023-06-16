
from random import randint


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
    prime = is_prime(number)
    right_answer = 'no'
    if prime:
        right_answer = 'yes'

    question_string = f'Question: {number}'

    return (question_string, right_answer)
