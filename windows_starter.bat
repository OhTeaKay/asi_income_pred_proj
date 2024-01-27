@echo off
python -m venv venv
call .\venv\Scripts\activate
pip install -r asi-income-prediction\requirements.txt
streamlit run asi-income-prediction\run_project.py
pause
