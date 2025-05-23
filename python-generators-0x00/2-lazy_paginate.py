import mysql.connector

# ---------- CONFIGURATION ----------
HOST = "localhost"
USER = "root"
PASSWORD = "your_password"  # 🔁 Replace this
DB_NAME = "ALX_prodev"
TABLE_NAME = "user_data"
# ----------------------------------

# Helper function: Fetch a single page
def paginate_users(page_size, offset):
    connection = mysql.connector.connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
        database=DB_NAME
    )
    cursor = connection.cursor(dictionary=True)

    query = f"SELECT * FROM user_data LIMIT %s OFFSET %s"
    cursor.execute(query, (page_size, offset))
    rows = cursor.fetchall()

    cursor.close()
    connection.close()

    return rows

# Generator: Lazily paginate users
def lazy_paginate(page_size):
    offset = 0
    while True:  # Single loop only
        page = paginate_users(page_size, offset)
        if not page:
            break
        yield page
        offset += page_size

# ---------- Optional: Run ----------
if __name__ == "__main__":
    for page in lazy_paginate(5):  # Fetch 5 users per page
        print("New Page:")
        for user in page:
            print(user)

