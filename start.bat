@echo off
echo Activating Virtual Environment...
call .\venv\Scripts\activate

echo Setting Environment Variables...
set KMP_DUPLICATE_LIB_OK=TRUE

echo Running the script...
python loopmaker.py

echo Script finished. Deactivating Virtual Environment...
call .\venv\Scripts\deactivate

echo Done.
pause
