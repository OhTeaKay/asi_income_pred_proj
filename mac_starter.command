#!/bin/bash
python -m venv venv
source venv/bin/activate
pip install -r asi-income-prediction/requirements.txt
streamlit run asi-income-prediction/run_project.py
