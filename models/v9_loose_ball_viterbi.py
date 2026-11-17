"""Model v9: Viterbi with the loose-ball and interrupted-stoppage dead-ball rules.

    .\\.venv\\Scripts\\python.exe models\\v9_loose_ball_viterbi.py       # -> evaluation/results/v9.csv

The v9 configuration of the current pipeline: none of the v12 additions (goalkeeper fix, ball out
while lost, touch gate) and no whistle (v14). Checked: its output is byte-identical to the file the
v9 commit produced.
"""

import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path[:0] = [os.path.join(ROOT, d) for d in ("models", "features", "tools")]
sys.path.insert(0, ROOT)
import params as P  # noqa: E402

P.USE_GK_FIX = False
P.USE_OOB_GAP = False
P.USE_TOUCH_GATE = False
P.USE_WHISTLE = False

import v14_whistle_viterbi as pipeline  # noqa: E402

if __name__ == "__main__":
    pipeline.main(default_name="v9")
