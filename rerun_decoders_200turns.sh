#!/bin/zsh
# Decoder evaluations under the batch spec: 8 decoders, 200 shared turns, no clock, $40 safety cap.
# Idempotent: skips any (run, condition) that already has an evaluation with those settings that
# was not cut short by an API error or interruption, so it can be rerun after a key swap.
set -e
cd /Users/emmakrentz/code/swarm-glyphs/erafkin-swarm-glyphs
SPEC=(--agents 8 --max-turns 200 --no-clock --max-cost-usd 40)

ensure_round2() {  # $1 human seed; prints the run dir
  local human=$1 seed=$(($1 - 1)) slot="experiments/tangut_200g_250l_200t/encoding/E0$1_sol_seed$1" run=""
  for d in $(ls -td logs/*_round_2/ 2>/dev/null); do
    if [ -f "$d/summary.json" ] && .venv/bin/python -c "import json,sys; c=json.load(open('$d/config.json')); sys.exit(0 if c['seed']==$seed and c.get('task_win_condition') else 1)"; then run="$d"; break; fi
  done
  if [ -z "$run" ]; then
    echo "=== seed $human round 2 start $(date +%H:%M:%S) ===" >&2
    .venv/bin/python -m src.enc_dec.run "configs/storm_shelter_tangut_200_wincond_seed${human}.json" --language-file "$slot/handoff/swarmish.txt" >&2
    run=$(ls -td logs/*_round_2/ | head -1)
  fi
  echo "$run"
}

eval_done() {  # $1 run dir, $2 condition
  .venv/bin/python - "$1" "$2" <<'PY'
import json, glob, sys
run, cond = sys.argv[1], sys.argv[2]
for d in glob.glob(f"{run.rstrip('/')}/monitor_runs/*/"):
    try:
        s = json.load(open(f"{d}/monitor_summary.json")); c = json.load(open(f"{d}/monitor_config.json"))
    except FileNotFoundError:
        continue
    if (s.get("conditions_requested") == [cond] and c.get("monitor_max_turns") == 200 and c.get("monitor_minutes") is None
            and c.get("monitor_n_agents") == 8 and s.get("stop_reason") not in ("api_error", "interrupted_or_failed", "usage_cost_missing")):
        sys.exit(0)
sys.exit(1)
PY
}

run_eval() {  # $1 label, $2 run dir, $3 condition
  if eval_done "$2" "$3"; then echo "=== $1 $3: already done under the 200-turn spec ==="; return; fi
  echo "=== $1 $3 start $(date +%H:%M:%S) ==="
  .venv/bin/python -m src.enc_dec.monitor "$2" "${SPEC[@]}" --condition "$3"
}

# Seed 1 baseline (no win condition): the earlier playthrough.
for cond in task_full no_task; do run_eval "seed 1 baseline" logs/20261107_182828_21003ef6 $cond; done
# Seed 2 win condition: only the no-task evaluation was cut off.
run_eval "seed 2 win" logs/20261107_231447_68be954a_round_2 no_task
# Seed 3 win condition: both were cut off.
for cond in task_full no_task; do run_eval "seed 3 win" logs/20261107_232807_70261c00_round_2 $cond; done
# Seed 4 win condition: the no-task evaluation was interrupted.
run_eval "seed 4 win" logs/20261108_001247_6a3a1f44_round_2 no_task
# Seed 5 win condition: round 2 first, then both evaluations.
run5=$(ensure_round2 5)
echo "SEED5_RUN=$run5"
for cond in task_full no_task; do run_eval "seed 5 win" "$run5" $cond; done
echo "=== all eight evaluations done $(date +%H:%M:%S) ==="
