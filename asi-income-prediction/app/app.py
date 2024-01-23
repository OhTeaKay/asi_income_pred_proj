import streamlit as st
import pandas as pd
import pickle
import os

def normalize(minmax_data, column_name, value):
    if pd.api.types.is_numeric_dtype(minmax_data[column_name]):
        min_val = minmax_data.at['min', column_name]
        max_val = minmax_data.at['max', column_name]
        if max_val != min_val:
            normalized_value = (value - min_val) / (max_val - min_val)
            return normalized_value
        else:
            return value

def main():
    model_path = os.path.join(os.getcwd(), "data", "model_ASCI.pkl")
    with open(model_path, 'rb') as file:
        loaded_data = pickle.load(file)

    loaded_model = loaded_data['model']
    loaded_X_train_encoded = loaded_data['X_train_encoded']
    loaded_minmax_data = loaded_data['minmax_data']

    st.title("Income Prediction App")

    age = st.slider("Age", 18, 100)
    workclass = st.selectbox("Workclass", ["Private", "Self-emp-not-inc", "Self-emp-inc", "Federal-gov", "Local-gov", "State-gov", "Without-pay", "Never-worked"])
    fnlwgt = st.number_input('Final Weight (fnlwgt): ')
    educational_num = st.slider("Education Level", 1, 16)
    marital_status = st.selectbox("Marital Status", ['Divorced', 'Married-AF-spouse', 'Married-civ-spouse', 'Married-spouse-absent', 'Never-married', 'Separated', 'Widowed'])
    occupation = st.selectbox("Occupation", ['Farming-fishing', 'Protective-serv', 'Machine-op-inspct', 'Priv-house-serv', 'Adm-clerical', 'Exec-managerial', 'Prof-specialty', 'Tech-support', 'Sales', 'Other-service', 'Craft-repair', 'Handlers-cleaners', 'Transport-moving', 'Armed-Forces'])
    relationship = st.selectbox("Relationship", ['Husband', 'Unmarried', 'Not-in-family', 'Own-child', 'Wife', 'Other-relative'])
    race = st.selectbox("Race", ['White', 'Black', 'Asian-Pac-Islander', 'Other', 'Amer-Indian-Eskimo'])
    gender = st.selectbox("Gender", ['Male', 'Female'])
    capital_gain = st.number_input("Capital Gain: ")
    capital_loss = st.number_input("Capital Loss: ")
    hours_per_week = st.number_input("Hours per Week: ")
    native_country = st.selectbox("Native Country", ['United-States', 'Holand-Netherlands', 'Mexico', 'Dominican-Republic', 'Ireland', 'Philippines', 'Puerto-Rico', 'Germany', 'Japan', 'India', 'Cambodia', 'Poland', 'Laos', 'England', 'Cuba', 'Haiti', 'South', 'Italy', 'Canada', 'Portugal', 'China', 'El-Salvador', 'Honduras', 'Iran', 'Guatemala', 'Nicaragua', 'Yugoslavia', 'Vietnam', 'Columbia', 'Hong', 'Greece', 'Peru', 'Thailand', 'Trinadad&Tobago', 'Scotland', 'Taiwan', 'Ecuador', 'Jamaica', 'Outlying-US(Guam-USVI-etc)', 'Hungary', 'France'])

    if st.button("Predict"):
        gain_per_hour = capital_gain / hours_per_week if hours_per_week != 0 else 0
        input_data = pd.DataFrame({
            'age': [normalize(loaded_minmax_data, 'age', age)],
            'fnlwgt': [normalize(loaded_minmax_data, 'fnlwgt', fnlwgt)],
            'educational-num': [normalize(loaded_minmax_data, 'educational-num', educational_num)],
            'workclass': [workclass],
            'marital-status': [marital_status],
            'occupation': [occupation],
            'relationship': [relationship],
            'race': [race],
            'gender': [gender],
            'capital-gain': [normalize(loaded_minmax_data, 'capital-gain', capital_gain)],
            'capital-loss': [normalize(loaded_minmax_data, 'capital-loss', capital_loss)],
            'hours-per-week': [normalize(loaded_minmax_data, 'hours-per-week', hours_per_week)],
            'native-country': [native_country],
            'gain-per-hour': [normalize(loaded_minmax_data, 'gain-per-hour', gain_per_hour)]
        })


        input_data_encoded = pd.get_dummies(input_data, columns=['workclass', 'marital-status', 'occupation', 'relationship', 'race', 'gender', 'native-country'], drop_first=True)
        for col in loaded_X_train_encoded:
            if col not in input_data_encoded.columns:
                input_data_encoded[col] = 0

        prediction = loaded_model.predict(input_data_encoded)
        st.write(f"The predicted income is: {prediction}")

if __name__ == "__main__":
    main()
