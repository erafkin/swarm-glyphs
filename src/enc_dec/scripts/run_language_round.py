"""
Language handoff experiment with a custom text task. The creation team does not know the task.
A new team then gets swarmish.txt and the task. The monitor reads only the new team's chat under
the briefings listed in src/enc_dec/prompts/round3_config.json.

The task text in the configs is a placeholder. Replace task_prompt, and the task texts in
src/enc_dec/prompts/round3_config.json, before treating a run as data.

Usage:
  .venv/bin/python -m src.enc_dec.scripts.run_language_round src/enc_dec/scripts/language_tangut.json
  .venv/bin/python -m src.enc_dec.scripts.run_language_round src/enc_dec/scripts/language_latin.json
"""

import argparse
from pathlib import Path

from src.enc_dec.config import LanguageExperimentConfig
from src.enc_dec.run import run_config

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("config", type=Path)
    run_config(LanguageExperimentConfig.from_file(parser.parse_args().config))
