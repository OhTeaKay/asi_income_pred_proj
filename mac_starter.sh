#!/bin/bash

# Activate echo to display commands
set -x

# Create a virtual environment
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate

# Install required packages
pip install -r asi-income-prediction/requirements.txt

# Change to the project directory
cd asi-income-prediction

# Run the Streamlit application
streamlit run run_project.py

# Wait for a user input before closing the script
read -p "Press any key to continue..."
