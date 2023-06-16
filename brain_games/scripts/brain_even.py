#!/usr/bin/env python3

from brain_games.cli import welcome_user
from brain_games.engine.command import run_game
from brain_games.games.even_code import generate_question

from brain_games.engine.command import welcome, final_message
QUESTIONS_COUNT = 3
TASK = 'Answer "yes" if the number is even, otherwise answer "no".'


def main():
    welcome()
    name = welcome_user()
    print(TASK)
    result = run_game(QUESTIONS_COUNT, generate_question)
    final_message(result, name)
    return


if __name__ == '__main__':
    main()
