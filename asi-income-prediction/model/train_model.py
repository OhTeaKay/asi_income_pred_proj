import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import os

def main():
    # Set the path to your data directory
    data_dir = os.path.join(os.getcwd(), "data")
    data_path = os.path.join(data_dir, 'filtered_data_normalized.csv')

    # Load preprocessed data
    data = pd.read_csv(data_path)

    # Preparing the data for training
    X = data.drop(['education', 'income'], axis=1)  # Adjust if other columns need to be dropped
    y = data['income']

    # Encoding categorical data and splitting the dataset
    X_encoded = pd.get_dummies(X, drop_first=True)
    X_train, X_test, y_train, y_test = train_test_split(X_encoded, y, test_size=0.2, random_state=42)

    # Training the model
    model = LogisticRegression()
    model.fit(X_train, y_train)

    filtered_data_path = os.path.join(data_dir, 'filtered_data.csv')
    search_for_minmax_data = pd.read_csv(filtered_data_path)
    # Select only numerical columns
    numerical_columns = search_for_minmax_data.select_dtypes(include='number')
    minmax_data = numerical_columns.describe().loc[['min', 'max']]

    # Evaluating the model
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    confusion = confusion_matrix(y_test, y_pred)
    report = classification_report(y_test, y_pred)
    print(f'Accuracy: {accuracy}')
    print('Confusion Matrix:\n', confusion)
    print('Classification Report:\n', report)

    # Saving the model
    model_filename = os.path.join(data_dir, 'model_ASCI.pkl')
    with open(model_filename, 'wb') as file:
        saved_data = {
            'model': model,
            'X_train_encoded': X_train,
            'minmax_data': minmax_data
        }
        pickle.dump(saved_data, file)

if __name__ == "__main__":
    main()
