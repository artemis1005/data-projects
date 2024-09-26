import pandas as pd

def extract_data(file_path):
    return pd.read_csv(file_path)

def clean_data(df):
    df.fillna(method='ffill', inplace=True)
    df.dropna(subset=['Age'], inplace=True)
    return df

def load_data(df, output_path):
    df.to_csv(output_path, index=False)

if __name__ == "__main__":
    # Extract
    df = extract_data('data/titanic.csv')
    
    # Clean
    df_cleaned = clean_data(df)
    
    # Load
    load_data(df_cleaned, 'data/titanic_cleaned.csv')
