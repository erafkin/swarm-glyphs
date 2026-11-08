"""Execute the three authorized revised Storm Shelter playthroughs, once each, sequentially."""
import json
import os
from pathlib import Path
import subprocess
from datetime import datetime, timezone

REPO = Path('/Users/ttaylor/Desktop/aiaf-hackathon/swarm-glyphs')
HERE = Path(__file__).resolve().parent
BATCH = REPO / 'experiments/tangut_200g_250l_200t'
PYTHON = REPO / '.venv/bin/python'
RUNS = ['R06', 'R07', 'R08']

def now():
    return datetime.now(timezone.utc).isoformat()

def save(state):
    pending = HERE / 'queue_state.json.tmp'
    pending.write_text(json.dumps(state, indent=2) + '\n')
    pending.replace(HERE / 'queue_state.json')

def main():
    if (HERE / 'queue_state.json').exists():
        raise RuntimeError('Queue already initialized; refusing a duplicate launch')
    manifest = json.loads((BATCH / 'batch.json').read_text())
    dirs = {r['id']: BATCH / r['path'] for r in manifest['runs']}
    for run_id in RUNS:
        config = json.loads((dirs[run_id] / 'config.json').read_text())
        if config.get('task_max_turns') != 200 or config.get('max_cost_usd') != 50 or config.get('task_minutes') is not None:
            raise RuntimeError(f'{run_id} limits differ from authorized settings')
        if any((dirs[run_id] / n).exists() for n in ('execution.json', 'receipt.json')):
            raise RuntimeError(f'{run_id} already launched or collected')
    state = {'status': 'running', 'started_at': now(), 'pid': os.getpid(),
             'runs': RUNS, 'current': None, 'completed': [], 'failed': None,
             'git_commit': subprocess.check_output(['git','rev-parse','HEAD'], cwd=REPO, text=True).strip()}
    save(state)
    for run_id in RUNS:
        folder = dirs[run_id]
        console = HERE / (run_id + '.console.log')
        state.update(current=run_id, current_started_at=now(), current_console=str(console))
        save(state)
        with console.open('x') as out:
            process = subprocess.Popen([str(PYTHON), '-u', str(BATCH / 'batch.py'), 'run', run_id],
                                       cwd=REPO, stdout=out, stderr=subprocess.STDOUT)
            state['current_pid'] = process.pid
            save(state)
            code = process.wait()
        receipt_path = folder / 'receipt.json'
        receipt = json.loads(receipt_path.read_text()) if receipt_path.exists() else None
        stop = receipt.get('stop_reason', '') if receipt else ''
        if code != 0 or not receipt or receipt.get('summary', {}).get('cost_incomplete') or stop.startswith('fatal_api_error') or stop == 'interrupted':
            state.update(status='needs_review', failed=run_id, returncode=code,
                         current_pid=None, finished_at=now(), message='Outputs preserved; subsequent runs unstarted.')
            save(state)
            return 1
        state['completed'].append({'id': run_id, 'finished_at': now(),
            'receipt': str(receipt_path), 'raw_path': receipt['raw_path'],
            'calls': receipt['discussion_calls'], 'turns_scheduled': receipt['summary'].get('task_turns_scheduled'), 'cost_usd': receipt['summary'].get('total_cost_usd'),
            'stop_reason': stop, 'escaped': receipt['summary'].get('escape_room',{}).get('escaped',False)})
        save(state)
    state.update(status='completed', current=None, current_pid=None, finished_at=now())
    save(state)
    return 0

if __name__ == '__main__':
    try:
        raise SystemExit(main())
    except Exception as exc:
        path = HERE / 'queue_state.json'
        state = json.loads(path.read_text()) if path.exists() else {}
        if state.get('pid') == os.getpid() or not path.exists():
            state.update(status='needs_review', failed=state.get('current'), finished_at=now(),
                         error=type(exc).__name__ + ': ' + str(exc))
            save(state)
        raise
