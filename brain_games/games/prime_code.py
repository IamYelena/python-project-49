import prompt
from random import randint
from brain_games.engine.command import proccessing_result


COUNT_OF_QUESTION = 3
TASK = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def generate_questions():
    print(TASK)
    for i in range(COUNT_OF_QUESTION):
        res1 = generate_question()
        if res1 is False:
            return False
    return True


def is_prime(number):
    if number == 1:
        return False
    for i in range(2, number - 1):
        if (number % i == 0):
            return False
    return True


def generate_question():
    number = randint(1, 100)
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
