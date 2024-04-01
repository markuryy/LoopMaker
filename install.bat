@echo off
echo Setting up Virtual Environment...
if not exist ".\venv" (
    python -m venv venv
    echo Virtual Environment created.
) else (
    echo Virtual Environment already exists.
)

echo Activating Virtual Environment...
call .\venv\Scripts\activate

echo Installing dependencies from requirements.txt...
pip install -r requirements.txt

echo Setup completed successfully.
call .\venv\Scripts\deactivate

echo Done.
pause
