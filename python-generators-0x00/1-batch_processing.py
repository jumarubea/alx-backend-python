import mysql.connector

# ---------- CONFIGURATION ----------
HOST = "localhost"
USER = "root"
PASSWORD = "password"
DB_NAME = "ALX_prodev"
TABLE_NAME = "user_data"
# ----------------------------------

# 1. Stream data in batches
def stream_users_in_batches(batch_size):
    connection = mysql.connector.connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
        database=DB_NAME
    )
    cursor = connection.cursor(dictionary=True)
    cursor.execute(f"SELECT * FROM user_data")

    while True:
        batch = cursor.fetchmany(batch_size)
        if not batch:
            break
        return batch  # Yield a full batch (list of dicts)

    cursor.close()
    connection.close()

# 2. Process each batch (filter users over age 25)
def batch_processing(batch_size):
    for batch in stream_users_in_batches(batch_size):  # Loop 1
        for user in batch:  # Loop 2 (nested)
            if float(user["age"]) > 25:
                yield user  # Yield users who meet the condition

# ---------- Optional: Run ----------
if __name__ == "__main__":
    print("Users over age 25:")
    for user in batch_processing(10):  # Loop 3 (output)
        print(user)

