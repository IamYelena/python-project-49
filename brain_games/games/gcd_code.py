import prompt

from random import randint
import math

def generate_questions():
    print("Find the greatest common divisor of given numbers.")
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
    
def generate_question():
    int1 = randint(1,100)
    int2 = randint(1,100)
    print(f'Question: {int1} {int2}')
    user_answer = prompt.string("Your answer:  ")
    right_answer = math.gcd(int1, int2)
    print_result(user_answer,right_answer)

    if str(user_answer) == str(right_answer):
        return True
    else:
        return False   
    
def print_result(user_answer,right_answer):
    if str(user_answer) == str(right_answer):
        print("Correct!")
    else:
        print(f'Your answer:  {user_answer}')
        print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{right_answer}'. ")
    