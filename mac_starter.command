#!/bin/bash
python -m venv venv
source venv/bin/activate
pip install -r asi-income-prediction/requirements.txt
cd asi-income-prediction
streamlit run run_project.py
