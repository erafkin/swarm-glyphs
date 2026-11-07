"""
Per-feature feedback test run, seed 0 (goal is person 22's features), 8 agents on GPT-6.1 Sol.
Stops when every agent has every feature right or total cost reaches $50.

Usage: .venv/bin/python -m src.scripts.run_features_seed0 [config.json]
  default config: features_seed0.json; features_seed0_no_spaces.json forbids spaces and agent IDs in chat.
"""

import argparse
from pathlib import Path

from src.config import GameConfig
from src.gameplay.play_game import run_config

DEFAULT_CONFIG = Path(__file__).with_name("features_seed0.json")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("config", nargs="?", type=Path, default=DEFAULT_CONFIG)
    run_config(GameConfig.from_file(parser.parse_args().config))
