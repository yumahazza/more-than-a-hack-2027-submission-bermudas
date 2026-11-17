"""Model v1: Viterbi with the loose-ball and interrupted-stoppage dead-ball rules.

    .\\.venv\\Scripts\\python.exe models\\v1_loose_ball_viterbi.py       # -> evaluation/results/v1.csv

The v1 configuration of the current pipeline: none of the v2 additions (goalkeeper fix, ball out
while lost, touch gate) and no whistle (v3).
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

import v3_whistle_viterbi as pipeline  # noqa: E402

if __name__ == "__main__":
    pipeline.main(default_name="v1")
