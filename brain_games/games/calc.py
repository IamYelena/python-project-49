from random import randint, choice
TASK = 'What is the result of the expression?'


MIN_NUMBER = 1
MAX_NUMBER = 30


def generate_question():
    number1 = randint(MIN_NUMBER, MAX_NUMBER)
    number2 = randint(MIN_NUMBER, MAX_NUMBER)
    operator = choice(['+', '-', '*'])
    question_string = f': {number1} {operator} {number2}'
    if operator == '+':
        right_answer = number1 + number2
    elif operator == '-':
        right_answer = number1 - number2
    else:
        right_answer = number1 * number2
    return (question_string, right_answer)
