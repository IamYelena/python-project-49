import prompt
from random import randint
from brain_games.engine.command import proccessing_result, run_game


QUESTIONS_COUNT = 3
MAX_NUMBER = 100
MIN_NUMBER = 1
TASK = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def generate_questions():
    print(TASK)
    res = run_game(QUESTIONS_COUNT, generate_question)
    return res


def is_prime(number):
    if number == 1:
        return False
    for i in range(2, number - 1):
        if (number % i == 0):
            return False
    return True


def generate_question():
    number = randint(MIN_NUMBER, MAX_NUMBER)
    prime = is_prime(number)
    right_answer = "no"
    if prime:
        right_answer = "yes"

    print(f'Question: {number}')
    user_answer = ''
    while user_answer == '':
        user_answer = prompt.string('Your answer:  ')

    result = proccessing_result(user_answer, right_answer)
    return result
