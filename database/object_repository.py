from models.object import Object


class ObjectRepository:

    def __init__(self, database):

        self.db = database

    def save_object(self, obj):

        self.db.cursor.execute(
            """
            INSERT OR IGNORE INTO objects(name)
            VALUES(?)
            """,
            (obj.name,)
        )

        self.db.connection.commit()

    def save_objects(self, objects):

        for obj in objects:
            self.save_object(obj)

    def load_objects(self):

        self.db.cursor.execute(
            """
            SELECT name
            FROM objects
            ORDER BY name
            """
        )

        rows = self.db.cursor.fetchall()

        objects = []

        for row in rows:
            objects.append(
                Object(
                    name=row[0]
                )
            )

        return objects