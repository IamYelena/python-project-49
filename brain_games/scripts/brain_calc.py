#!/usr/bin/env python3


import brain_games.games.calc as game_module
from brain_games.engine.command import run_game


def main():
    run_game(game_module)


if __name__ == '__main__':
    main()
