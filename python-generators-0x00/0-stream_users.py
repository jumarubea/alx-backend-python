import mysql.connector

# ---------- CONFIGURATION ----------
HOST = "localhost"
USER = "root"
PASSWORD = "your_password"  # 🔁 Replace with your MySQL password
DB_NAME = "ALX_prodev"
TABLE_NAME = "user_data"
# ----------------------------------

def stream_users():
    connection = mysql.connector.connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
        database=DB_NAME
    )
    cursor = connection.cursor(dictionary=True)
    cursor.execute(f"SELECT * FROM {TABLE_NAME}")
    
    # Use a single loop to yield one row at a time
    for row in cursor:
        yield row

    cursor.close()
    connection.close()

# Optional: for testing
if __name__ == "__main__":
    for user in stream_users():
        print(user)

