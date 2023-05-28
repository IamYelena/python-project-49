#!/usr/bin/env python3

from brain_games.cli import welcome_user
from brain_games.games.prime_code import generate_questions
from brain_games.engine.command import welcome, final_message


def main():
    welcome()
    name = welcome_user()
    result = generate_questions()
    final_message(result, name)
    return


if __name__ == '__main__':
    main()
