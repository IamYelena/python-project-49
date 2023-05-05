#!/usr/bin/env python3

from brain_games.cli import welcome_user
from random import randint
import prompt

def welcome():
    print("Welcome to the Brain Games!")


def main():
    welcome()
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    r1 = random_work(name)
    if (r1 == False):
        return
    r2 = random_work(name)
    if (r2 == False):
        return
    r3 = random_work(name)
    if (r3 == False):
        return
    print("Congratulations, " + name + "!")

    
def random_work(name):
    v = randint(0, 100)
    print("Question: " + str(v))
    answer = ''
    while answer == '':
        answer = prompt.string('Your answer:  ')
        
    r_answer = ''
    if (answer == "yes"):
        r_answer = "no"
    if (answer == "no"):
        r_answer = "yes"
    if (v % 2 == 0 and answer == "yes"):
        print("Correct!")
        return True
    if (v % 2 != 0 and answer == "no"):
        print("Correct!")
        return True
    r = "'" + answer + "' is wrong answer ;(. Correct answer was '" + r_answer + "'." 
    print(r)
    print("Let's try again, " + name + "!")
    return False


if __name__ == '__main__':
    main()
