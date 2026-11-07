"""
Board (Guess Who) test run, seed 0 (goal c5cfd9c4..., formerly person 22), 8 agents on GPT-6.1 Sol.
Stops when every agent guesses the right person or total cost reaches $50.

Usage: .venv/bin/python -m src.scripts.run_board_seed0
"""

from pathlib import Path

from src.config import GameConfig
from src.gameplay.play_game import run_config

if __name__ == "__main__":
    run_config(GameConfig.from_file(Path(__file__).with_name("board_seed0.json")))
