import sys
from pylint import lint

THRESHOLD = 5

run = lint.Run(["app.py", "model.py"], exit=False)
score = run.linter.stats.global_note
if score < THRESHOLD:
    print("Linter score above threshold value: FAILED")
    sys.exit(1)

sys.exit(0)
