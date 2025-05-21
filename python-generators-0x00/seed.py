import csv
import mysql.connector
from mysql.connector import errorcode

# ---------- CONFIGURATION ----------
HOST = "localhost"
USER = "root"
PASSWORD = "password"
DB_NAME = "ALX_prodev"
TABLE_NAME = "user_data"
CSV_FILE = "user_data.csv"
# ----------------------------------

# 1. Connect to MySQL server
def connect_db():
    return mysql.connector.connect(
        host=HOST,
        user=USER,
        password=PASSWORD
    )

# 2. Create database if it doesn't exist
def create_database(connection):
    cursor = connection.cursor()
    try:
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}")
        print(f"Database '{DB_NAME}' ready.")
    except mysql.connector.Error as err:
        print(f"Failed creating database: {err}")
    finally:
        cursor.close()

# 3. Connect to the ALX_prodev database
def connect_to_prodev():
    return mysql.connector.connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
        database=DB_NAME
    )

# 4. Create user_data table
def create_table(connection):
    cursor = connection.cursor()
    query = f"""
    CREATE TABLE IF NOT EXISTS {TABLE_NAME} (
        user_id CHAR(36) PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        email VARCHAR(255) NOT NULL,
        age DECIMAL NOT NULL,
        INDEX (user_id)
    )
    """
    cursor.execute(query)
    print(f"Table '{TABLE_NAME}' is ready.")
    cursor.close()

# 5. Insert data if not already present
def insert_data(connection, data):
    cursor = connection.cursor()
    insert_query = f"""
    INSERT IGNORE INTO {TABLE_NAME} (user_id, name, email, age)
    VALUES (%s, %s, %s, %s)
    """
    cursor.executemany(insert_query, data)
    connection.commit()
    print(f"Inserted {cursor.rowcount} rows.")
    cursor.close()

# 6. Read data from CSV
def read_csv_data(filename):
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        return [
            (row['user_id'], row['name'], row['email'], row['age'])
            for row in reader
        ]

# ---------- RUN SEED SCRIPT ----------
if __name__ == "__main__":
    root_conn = connect_db()
    create_database(root_conn)
    root_conn.close()

    db_conn = connect_to_prodev()
    create_table(db_conn)

    data = read_csv_data(CSV_FILE)
    insert_data(db_conn, data)

    db_conn.close()

