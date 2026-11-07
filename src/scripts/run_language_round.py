"""
Language handoff experiment. The creation team does not know the task. A new team then gets their
language descriptions and the task. A monitor reads only the new team's chat under four briefings.

The task text in the configs is a placeholder. Replace task_prompt, wrong_task_far, and
wrong_task_near before treating a run as data.

Usage:
  .venv/bin/python -m src.scripts.run_language_round src/scripts/language_glyphs.json
  .venv/bin/python -m src.scripts.run_language_round src/scripts/language_free.json
"""

import argparse
from pathlib import Path

from src.language_round.config import LanguageExperimentConfig
from src.language_round.run import run_config

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("config", type=Path)
    run_config(LanguageExperimentConfig.from_file(parser.parse_args().config))
