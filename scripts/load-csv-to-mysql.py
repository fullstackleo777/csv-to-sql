import mysql.connector
import pandas as pd
import json
import os

# File paths
config_path = '../config/db_config.json'
csv_path = '../data/processed/processed_data.csv'

# Load DB config
def load_config():
    with open(config_path, 'r') as file:
        return json.load(file)

# Connect to MySQL and load CSV
def load_csv_to_mysql():
    config = load_config()

    # Connect to MySQL
    conn = mysql.connector.connect(
        host=config['host'],
        user=config['user'],
        password=config['password'],
        database=config['database']
    )
    cursor = conn.cursor()

    # Load CSV
    df = pd.read_csv(csv_path)
    for _, row in df.iterrows():
        cursor.execute("""
            INSERT INTO example (id, name, age, email)
            VALUES (%s, %s, %s, %s)
        """, (row['id'], row['name'], row['age'], row['email']))

    conn.commit()
    cursor.close()
    conn.close()
    print("Data successfully loaded into MySQL!")

if __name__ == "__main__":
    load_csv_to_mysql()
