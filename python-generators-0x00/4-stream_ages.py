import mysql.connector

HOST = "localhost"
USER = "root"
PASSWORD = "password"
DB_NAME = "ALX_prodev"
TABLE_NAME = "user_data"


def connect_to_prodev():
    return mysql.connector.connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
        database=DB_NAME
    )


def stream_user_ages(connection):
    cursor = connection.cursor()
    cursor.execute(f"SELECT age FROM TABLE_NAM}")
    for (age,) in cursor:
        yield float(age)
    cursor.close()
    

def calculate_average_age():
    connection = connect_to_prodev()
    total = 0
    count = 0

    for age in stream_user_ages(connection):
        total += age
        count += 1

    connection.close()

    if count == 0:
        print("No users found.")
    else:
        average = total / count
        print(f"Average age of users: {average:.2f}")

# ---------- RUN SCRIPT ----------
if __name__ == "__main__":
    calculate_average_age()

