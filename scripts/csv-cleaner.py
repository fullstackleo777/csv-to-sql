import pandas as pd

# File paths
raw_csv_path = '../data/raw/example_data.csv'
processed_csv_path = '../data/processed/processed_data.csv'

# Process raw CSV
def clean_csv():
    df = pd.read_csv(raw_csv_path)
    df.drop_duplicates(inplace=True)  # Remove duplicates
    df.fillna({'age': 0, 'email': 'unknown@example.com'}, inplace=True)  # Fill missing values
    df.to_csv(processed_csv_path, index=False)
    print(f"Processed data saved to {processed_csv_path}")

if __name__ == "__main__":
    clean_csv()
