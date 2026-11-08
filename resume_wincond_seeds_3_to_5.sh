#!/bin/zsh
# Resume the win-condition batch for seeds 3, 4 and 5. Safe to rerun: it skips any round 2 run or
# evaluation that already completed, so it picks up wherever the batch was paused.
set -e
cd /Users/emmakrentz/code/swarm-glyphs/erafkin-swarm-glyphs
for human in 3 4 5; do
  seed=$((human - 1))
  slot="experiments/tangut_200g_250l_200t/encoding/E0${human}_sol_seed${human}"
  run=""
  for d in $(ls -td logs/*_round_2/ 2>/dev/null); do
    if [ -f "$d/summary.json" ] && .venv/bin/python -c "import json,sys; c=json.load(open('$d/config.json')); sys.exit(0 if c['seed']==$seed and c.get('task_win_condition') else 1)"; then run="$d"; break; fi
  done
  if [ -z "$run" ]; then
    echo "=== seed $human round 2 start $(date +%H:%M:%S) ==="
    .venv/bin/python -m src.enc_dec.run "configs/storm_shelter_tangut_200_wincond_seed${human}.json" --language-file "$slot/handoff/swarmish.txt"
    run=$(ls -td logs/*_round_2/ | head -1)
  else
    echo "=== seed $human round 2 already complete: $run ==="
  fi
  echo "SEED${human}_RUN=$run"
  for cond in task_full no_task; do
    if .venv/bin/python - "$run" "$cond" <<'PY'
import json, glob, sys
run, cond = sys.argv[1], sys.argv[2]
for d in glob.glob(f"{run}/monitor_runs/*/"):
    try:
        s = json.load(open(f"{d}/monitor_summary.json"))
    except FileNotFoundError:
        continue
    if s.get("conditions_requested") == [cond] and (s.get("conditions_completed") or s.get("stop_reason") == "cost_limit_reached"):
        sys.exit(0)
sys.exit(1)
PY
    then echo "=== seed $human eval $cond already complete ==="; continue; fi
    echo "=== seed $human eval $cond start $(date +%H:%M:%S) ==="
    .venv/bin/python -m src.enc_dec.monitor "$run" --agents 8 --max-cost-usd 10 --condition "$cond"
  done
  echo "=== seed $human done $(date +%H:%M:%S) ==="
done
echo "=== all seeds done $(date +%H:%M:%S) ==="
