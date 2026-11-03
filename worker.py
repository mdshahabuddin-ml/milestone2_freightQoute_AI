"""Background worker: runs simulator/agent cycles beside the web server."""
import os, sys, time, traceback
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import config
import live_engine as LE

INTERVAL = float(os.environ.get("WORKER_INTERVAL", "10"))
CANDIDATES = ["run_cycle", "cycle", "tick", "simulate_step", "simulate",
              "step", "agent_cycle", "run_agents", "run_once"]

def log(*a):
    print("[worker]", *a, flush=True)

def find_steps():
    return [(n, getattr(LE, n)) for n in CANDIDATES if callable(getattr(LE, n, None))]

def main():
    log("started, kind =", getattr(config, "KIND", "?"))
    try:
        if hasattr(LE, "init_live_tables"):
            LE.init_live_tables()
    except Exception:
        log("init_live_tables failed:\n" + traceback.format_exc())

    steps = find_steps()
    if not steps:
        log("no cycle functions found in live_engine.py; idling")
    else:
        log("will call:", ", ".join(n for n, _ in steps))

    while True:
        for name, fn in steps:
            try:
                fn()
            except TypeError:
                log(f"{name}() needs arguments, skipping it")
            except Exception:
                log(f"{name}() failed:\n" + traceback.format_exc())
        time.sleep(INTERVAL)

if __name__ == "__main__":
    main()
