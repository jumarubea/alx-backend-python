import asyncio
import aiosqlite

DB_NAME = "async.db"

async def setup_database():
    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute("DROP TABLE IF EXISTS users")
        await db.execute("""
            CREATE TABLE users (
                id INTEGER PRIMARY KEY,
                name TEXT,
                age INTEGER
            )
        """)
        users = [
            ("Alice", 30),
            ("Bob", 45),
            ("Charlie", 50),
            ("Daisy", 25),
            ("Eve", 41)
        ]
        await db.executemany("INSERT INTO users (name, age) VALUES (?, ?)", users)
        await db.commit()

async def async_fetch_users():
    async with aiosqlite.connect(DB_NAME) as db:
        async with db.execute("SELECT * FROM users") as cursor:
            rows = await cursor.fetchall()
            print("All Users:")
            for row in rows:
                print(row)
            return rows

async def async_fetch_older_users():
    async with aiosqlite.connect(DB_NAME) as db:
        async with db.execute("SELECT * FROM users WHERE age > 40") as cursor:
            rows = await cursor.fetchall()
            print("Users older than 40:")
            for row in rows:
                print(row)
            return rows

async def fetch_concurrently():
    await setup_database()
    await asyncio.gather(
        async_fetch_users(),
        async_fetch_older_users()
    )

if __name__ == "__main__":
    asyncio.run(fetch_concurrently())

