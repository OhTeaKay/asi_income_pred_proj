import subprocess
import os

def run_script(script_path):
    result = subprocess.run(['python', script_path], stdout=subprocess.PIPE)
    print(result.stdout.decode())

def main():
    project_root = os.path.dirname(os.path.abspath(__file__))

    data_prep_path = os.path.join(project_root, 'data', 'data_preparation.py')
    model_train_path = os.path.join(project_root, 'model', 'train_model.py')
    app_path = os.path.join(project_root, 'app', 'app.py')

    print("Running Data Preparation...")
    run_script(data_prep_path)

    print("Running Model Training...")
    run_script(model_train_path)

    print("Starting Streamlit App...")
    subprocess.Popen(['streamlit', 'run', app_path])

if __name__ == "__main__":
    main()
