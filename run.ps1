# Path to venv
$venvPath = "$PSScriptRoot\venv"
$activateScript = "$venvPath\Scripts\Activate.ps1"

# 1. Create venv if missing
if (!(Test-Path $venvPath)) {
    Write-Host "venv not found — creating..."
    python -m venv $venvPath

    if (!(Test-Path $activateScript)) {
        Write-Host "Venv creation FAILED. Fix your Python install." -ForegroundColor Red
        exit 1
    }

    # Activate once to install dependencies
    Write-Host "Installing dependencies..."
    & $activateScript
    pip install pillow
    deactivate
}

# 2. Activate venv
Write-Host "Activating venv..."
& $activateScript

# 3. Run the screenshot script
Write-Host "Running autosnap.py..."
python "$PSScriptRoot\autosnap.py"

# 4. Keep window open
Read-Host "Press ENTER to exit"
