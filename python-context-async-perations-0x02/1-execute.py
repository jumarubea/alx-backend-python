import sqlite3

class ExecuteQuery:
    def __init__(self, db_name, query, params=None):
        self.db_name = db_name
        self.query = query
        self.params = params or []
        self.connection = None
        self.cursor = None
        self.results = None

    def __enter__(self):
        self.connection = sqlite3.connect(self.db_name)
        self.cursor = self.connection.cursor()
        self.cursor.execute(self.query, self.params)
        self.results = self.cursor.fetchall()
        return self.results

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.connection:
            self.connection.commit()
            self.connection.close()

if __name__ == "__main__":
    with sqlite3.connect('mydb.db') as conn:
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)")
        cur.execute("DELETE FROM users")
        cur.executemany("INSERT INTO users (name, age) VALUES (?, ?)", [
            ('Alice', 30),
            ('Bob', 22),
            ('Charlie', 28),
            ('Daisy', 19)
        ])
        conn.commit()

    query = "SELECT * FROM users WHERE age > ?"
    with ExecuteQuery('mydb.db', query, [25]) as results:
        print("Users older than 25:")
        for row in results:
            print(row)

