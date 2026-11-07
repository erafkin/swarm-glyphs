"""
Board (Guess Who) test run, seed 0 (goal person 22), 8 agents on GPT-6.1 Sol.
Stops when every agent guesses the right person or total cost reaches $50.

Usage: .venv/bin/python -m src.guess_who.scripts.run_board_seed0 [config.json]
  default config: board_seed0.json; board_seed0_no_spaces.json is the same run without spaces in chat.
"""

import argparse
from pathlib import Path

from src.guess_who.config import GameConfig
from src.guess_who.play_game import run_config

DEFAULT_CONFIG = Path(__file__).with_name("board_seed0.json")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("config", nargs="?", type=Path, default=DEFAULT_CONFIG)
    run_config(GameConfig.from_file(parser.parse_args().config))
