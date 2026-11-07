"""
Per-feature feedback test run, seed 0 (goal is c5cfd9c4...'s features, formerly person 22), 8 agents on GPT-6.1 Sol.
Stops when every agent has every feature right or total cost reaches $50.

Usage: .venv/bin/python -m src.scripts.run_features_seed0
"""

from pathlib import Path

from src.config import GameConfig
from src.gameplay.play_game import run_config

if __name__ == "__main__":
    run_config(GameConfig.from_file(Path(__file__).with_name("features_seed0.json")))
