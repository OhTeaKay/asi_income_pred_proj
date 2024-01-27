# data_preparation.py

import pandas as pd
import os

# Function to normalize numeric values
def normalize(values):
    if pd.api.types.is_numeric_dtype(values):
        min_val = values.min()
        max_val = values.max()
        if(max_val == min_val):
            return values
        return (values - min_val) / (max_val - min_val)
    else:
        # Handle non-numeric values
        return values

def main():
    # Set the path to your data directory
    data_dir = os.path.join(os.getcwd(), "data")
    base_data_path = os.path.join(data_dir, "adult.csv")

    # Load data
    base_data = pd.read_csv(base_data_path)

    # Data Exploration and Cleaning
    df = base_data
    df.eq('?').any()

    # Replace missing values and normalize data
    # Repeat this block for 'workclass', 'occupation', and 'native-country'
    for column in ['workclass', 'occupation', 'native-country']:
        numeric_columns = df.select_dtypes(include='number')
        numeric_columns[column] = df[column]
        normalizedvariance = numeric_columns.groupby(column).apply(lambda x: normalize(x).var())
        lowest_variance_column = normalizedvariance.idxmin(axis=1)

        median_capital_gain = df.groupby(column)['capital-gain'].mean()
        median_capital_gain = median_capital_gain.drop('?')
        df[column] = df[column].replace({'?': median_capital_gain.idxmin()})

    # Additional Data Processing
    df['gain-per-hour'] = df['capital-gain'] / df['hours-per-week']

    # Filtering and Normalizing Data
    conditions = {
        'age': [0.2, 0.8],
        'capital-gain': [0.2, 1],
        'capital-loss': [0.2, 1],
        'hours-per-week': [0.2, 0.99],
        'gain-per-hour': [0.2, 0.99]
    }

    filtered_df = df.copy()
    for col, (lower_quantile, upper_quantile) in conditions.items():
        filtered_df = filtered_df[(filtered_df[col] >= filtered_df[col].quantile(lower_quantile)) & (filtered_df[col] <= filtered_df[col].quantile(upper_quantile))]

    filtered_df_normalized = filtered_df.apply(lambda x: normalize(x))

    # Save processed data
    filtered_data_path = os.path.join(data_dir, 'filtered_data.csv')
    filtered_df.to_csv(filtered_data_path, index=False)

    filtered_data_normalized_path = os.path.join(data_dir, 'filtered_data_normalized.csv')
    filtered_df_normalized.to_csv(filtered_data_normalized_path, index=False)

if __name__ == "__main__":
    main()
