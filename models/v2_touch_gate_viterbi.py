"""Model v2: touch-gated Viterbi, without the referee whistle.

    .\\.venv\\Scripts\\python.exe models\\v2_touch_gate_viterbi.py       # -> evaluation/results/v2.csv

The same pipeline as v3 (models/v3_whistle_viterbi.py) with the whistle switched off:
goalkeeper team fix, ball out while the tracker had lost it, touch-gated team changes (ideas from
a teammate's branch, values derived by us; see params.py). Kept to show the step from v2 to v3.
"""

import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path[:0] = [os.path.join(ROOT, d) for d in ("models", "features", "tools")]
sys.path.insert(0, ROOT)
import params as P  # noqa: E402

P.USE_WHISTLE = False

import v3_whistle_viterbi as pipeline  # noqa: E402

if __name__ == "__main__":
    pipeline.main(default_name="v2")
