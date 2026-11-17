"""Model v12: touch-gated Viterbi, without the referee whistle.

    .\\.venv\\Scripts\\python.exe models\\v12_touch_gate_viterbi.py      # -> evaluation/results/v12.csv

The same pipeline as v14 (models/v14_whistle_viterbi.py) with the whistle switched off:
goalkeeper team fix, ball out while the tracker had lost it, touch-gated team changes (ideas from
a teammate's branch, values derived by us; see params.py). Kept to show the step from v12 to v14.
Checked: its output is byte-identical to the file the v12 commit produced.
"""

import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path[:0] = [os.path.join(ROOT, d) for d in ("models", "features", "tools")]
sys.path.insert(0, ROOT)
import params as P  # noqa: E402

P.USE_WHISTLE = False

import v14_whistle_viterbi as pipeline  # noqa: E402

if __name__ == "__main__":
    pipeline.main(default_name="v12")
