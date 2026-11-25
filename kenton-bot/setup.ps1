# One-command setup for Windows PowerShell:   .\setup.ps1
# (If scripts are blocked:  Set-ExecutionPolicy -Scope CurrentUser RemoteSigned)
$ErrorActionPreference = "Stop"

python --version
python -m venv .venv
. .\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
pip install -e .

# optional speed-up; ignore failure
try { pip install -r requirements-fast.txt } catch { Write-Host "eval7 not installed (optional) - continuing" }

python scripts/check_setup.py
Write-Host ""
Write-Host "Done. Next time, activate the environment with:  .\.venv\Scripts\Activate.ps1"
