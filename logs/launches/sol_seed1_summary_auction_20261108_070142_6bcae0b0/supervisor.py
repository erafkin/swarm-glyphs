import datetime, json, os, subprocess, sys
from pathlib import Path
repo, condition, status_path = sys.argv[1:]
status = {"condition": condition, "supervisor_pid": os.getpid(), "started_at": datetime.datetime.now(datetime.timezone.utc).isoformat()}
def save():
    p = Path(status_path)
    tmp = p.with_suffix(".tmp")
    tmp.write_text(json.dumps(status, indent=2) + "\n")
    tmp.replace(p)
try:
    child = subprocess.Popen([str(Path(repo) / "run_sol_seed1_contexts.sh"), "--run", condition], cwd=repo)
    status["child_pid"] = child.pid
    save()
    status["exit_code"] = child.wait()
except BaseException as exc:
    status["supervisor_error"] = repr(exc)
    raise
finally:
    status["finished_at"] = datetime.datetime.now(datetime.timezone.utc).isoformat()
    save()
