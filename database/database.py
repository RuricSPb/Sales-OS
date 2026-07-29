import sqlite3
from pathlib import Path


class Database:

    def __init__(self):

        Path("database").mkdir(exist_ok=True)

        self.connection = sqlite3.connect("database/sales_os.db")

        self.cursor = self.connection.cursor()

        self.create_tables()

    def create_tables(self):

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS objects (

                id INTEGER PRIMARY KEY AUTOINCREMENT,

                name TEXT UNIQUE
            )
        """)

        self.connection.commit()