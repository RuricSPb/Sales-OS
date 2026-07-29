import sqlite3
from pathlib import Path


class Database:

    def __init__(self):

        Path("database").mkdir(exist_ok=True)

        self.connection = sqlite3.connect("database/sales_os.db")

        self.connection.row_factory = sqlite3.Row

        self.cursor = self.connection.cursor()

        self.create_tables()

    def create_tables(self):

        self.cursor.execute("""

            CREATE TABLE IF NOT EXISTS objects(

                id INTEGER PRIMARY KEY AUTOINCREMENT,

                name TEXT UNIQUE,

                source TEXT,

                external_id TEXT,

                address TEXT,

                customer TEXT,

                contractor TEXT,

                designer TEXT,

                manager TEXT,

                status TEXT,

                comment TEXT

            )

        """)

        self.cursor.execute("""

            CREATE TABLE IF NOT EXISTS companies(

                id INTEGER PRIMARY KEY AUTOINCREMENT,

                object_id INTEGER,

                company_name TEXT,

                company_type TEXT,

                contact TEXT,

                phone TEXT,

                email TEXT,

                FOREIGN KEY(object_id)
                    REFERENCES objects(id)

            )

        """)

        self.connection.commit()