import pandas as pd
import os
from utils.common import load_yaml_config

def preprocess_data(config):
    config = load_yaml_config(config)
    prep_config = config['preprocess']
    
    input_path = prep_config['input_path']
    output_path = prep_config['output_path']
    drop_columns = prep_config.get('drop_columns', [])
    fillna_values = prep_config.get('fillna', {})

    df = pd.read_csv(input_path)

    # Drop specified columns
    if drop_columns:
        df = df.drop(columns=drop_columns)

    # Fill missing values
    for column, strategy in fillna_values.items():
        if strategy == "mean":
            df[column].fillna(df[column].mean(), inplace=True)
        elif strategy == "median":
            df[column].fillna(df[column].median(), inplace=True)
        elif strategy == "constant":
            df[column].fillna(strategy['value'], inplace=True)

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False)
    print(f"Preprocessed data saved to {output_path}")

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Data Preprocessing Script")
    parser.add_argument("--config", type=str, required=True, help="Path to configuration file")
    args = parser.parse_args()

    preprocess_data(args.config)