#!/usr/bin/env python3

from brain_games.engine.command import run_game
import brain_games.games.progression as game_module


def main():
    run_game(game_module)


if __name__ == '__main__':
    main()
