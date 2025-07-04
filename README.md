![CSV to SQL Cover Image](https://raw.githubusercontent.com/fullstackleo777/covers/refs/heads/main/covers/csv-to-sql/cover_csv-to-sql.png)

# csv-to-sql
Structural Starting Point for Data CSV to SQL Database Using CSV, MySQL, & Python - FullStackLeo

## Structure
~~~
csv-to-mysql-project/
│
├── data/
│   ├── raw/
│   │   └── example_data.csv
│   ├── processed/
│       └── processed_data.csv
│
├── scripts/
│   ├── csv_cleaner.py
│   ├── create_mysql_table.sql
│   ├── load_csv_to_mysql.py
│
├── config/
│   └── db_config.json
│
├── .gitignore
├── README.md
├── LICENSE
└── requirements.txt
~~~

## How to Use

1. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

2. **Prepare MySQL database**:
     Run the SQL script to create the table:
      ```bash
      mysql -u root -p my_database < scripts/create_mysql_table.sql
      ```

3. **Process the CSV**:
     Run the cleaner script:
      ```bash
      python scripts/csv_cleaner.py
      ```

4. **Load the CSV into MySQL**:
     Run the loader script:
      ```bash
      python scripts/load_csv_to_mysql.py
      ```

## Requirements
- Python 3.8+
- MySQL
- Required Python libraries (see `requirements.txt`).

## License
This project is licensed under the MIT License.

___
