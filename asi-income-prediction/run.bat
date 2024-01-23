@echo off

echo Running Data Preparation...
python "Z:\Projects_Oskar\Python_Projects\asi_income_prediction\data\data_preparation.py"

echo Running Model Training...
python "Z:\Projects_Oskar\Python_Projects\asi_income_prediction\model\train_model.py"

echo Starting Streamlit App...
streamlit run "Z:\Projects_Oskar\Python_Projects\asi_income_prediction\app\app.py"
