#!/usr/bin/env python3

from brain_games.engine.command import run_game
from brain_games.cli import welcome_user
from brain_games.engine.command import welcome, final_message
from brain_games.games.gcd_code import generate_question


QUESTIONS_COUNT = 3
TASK = 'Find the greatest common divisor of given numbers.'


def main():
    welcome()
    name = welcome_user()
    print(TASK)
    result = run_game(QUESTIONS_COUNT, generate_question)
    final_message(result, name)
    return


if __name__ == '__main__':
    main()
