#!/usr/bin/env bash
# One-command setup for Mac / Linux:   bash setup.sh
set -e

PY=${PYTHON:-python3}
echo "Using $($PY --version)"

$PY -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
pip install -e .

# optional speed-up; ignore failure
pip install -r requirements-fast.txt || echo "eval7 not installed (optional) - continuing"

python scripts/check_setup.py
echo
echo "Done. Next time, activate the environment with:  source .venv/bin/activate"
