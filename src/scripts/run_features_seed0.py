"""
Run a per-feature feedback experiment using the selected JSON config.
The default is seed 0, 8 GPT-6.1 Sol agents, and a $50 soft cost limit.
Stops when every agent has every feature right or the configured cost limit is reached.

Usage: .venv/bin/python -m src.scripts.run_features_seed0 [config.json]
  default config: features_seed0.json; features_seed0_no_spaces.json forbids spaces and agent IDs in chat.
  Gemini equivalent ($20 soft limit): features_seed0_no_spaces_gemini.json
  Mixed 4 Sol / 4 Gemini ($30 soft limit): features_seed0_no_spaces_mixed.json
  Current presets randomize feature ownership and score every 60 seconds.
  Five fresh Gemini runs ($20 each; run 1 then review): configs/gemini_random_features_5x60s/
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
