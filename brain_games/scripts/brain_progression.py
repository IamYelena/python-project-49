#!/usr/bin/env python3

from brain_games.cli import welcome_user
from brain_games.games.progression_code import generate_questions

import prompt

def welcome():
    print("Welcome to the Brain Games!")


def main():
    welcome()
    name = welcome_user()
    result = generate_questions()
    if result == True:
        print("Congratulations, " + name + "!")
    else:
        print("Let's try again, " + name + "!")
    return



if __name__ == '__main__':
    main()
