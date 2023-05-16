import prompt

from random import randint

def generate_questions():
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    res1 = generate_question()
    if res1 == False:
        return False
    res2 = generate_question()
    if res2 == False:
        return False
    res3 = generate_question()
    if res3 == False:
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
    number = randint(1,100)
    prime = is_prime(number)
    right_answer = "no"
    if prime:
        right_answer = "yes"

    print(f'Question: {number}')
    user_answer = ''
    while user_answer == '':
        user_answer = prompt.string('Your answer:  ')

    print_result(user_answer,right_answer)

    if str(user_answer) == str(right_answer):
        return True
    else:
        return False
            
    return False

def print_result(user_answer,right_answer):
    if str(user_answer) == str(right_answer):
        print("Correct!")
    else:
        print(f'Your answer:  {user_answer}')
        print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{right_answer}'. ")
    