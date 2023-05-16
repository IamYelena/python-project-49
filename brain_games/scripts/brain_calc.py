#!/usr/bin/env python3

from brain_games.games.calc_code import generate_questions
from brain_games.cli import welcome_user


def welcome():
    print("Welcome to the Brain Games!")


def main():
    welcome()
    name = welcome_user()

    result = generate_questions()
    if result is True:
        print("Congratulations, " + name + "!")
    else:
        print("Let's try again, " + name + "!")


if __name__ == '__main__':
    main()
