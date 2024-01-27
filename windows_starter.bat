@echo off
python -m venv venv
call .\venv\Scripts\activate
pip install -r asi-income-prediction\requirements.txt
cd asi-income-prediction
streamlit run run_project.py
pause
