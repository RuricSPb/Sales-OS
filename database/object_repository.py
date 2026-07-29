from models.object import Object


class ObjectRepository:

    def __init__(self, database):

        self.db = database

    def save_object(self, obj):

        self.db.cursor.execute(
            """
            INSERT OR IGNORE INTO objects
            (
                name,
                source,
                external_id,
                address,
                customer,
                contractor,
                designer,
                manager,
                status,
                comment
            )

            VALUES
            (
                ?,?,?,?,?,?,?,?,?,?
            )
            """,
            (
                obj.name,
                obj.source,
                obj.external_id,
                obj.address,
                obj.customer,
                obj.contractor,
                obj.designer,
                obj.manager,
                obj.status,
                obj.comment
            )
        )

        self.db.connection.commit()

        self.db.cursor.execute(
            """
            SELECT id
            FROM objects
            WHERE name = ?
            """,
            (obj.name,)
        )

        row = self.db.cursor.fetchone()

        if row:
            obj.id = row["id"]

        return obj

    def get_object(self, object_id):

        self.db.cursor.execute(
            """
            SELECT *
            FROM objects
            WHERE id = ?
            """,
            (object_id,)
        )

        row = self.db.cursor.fetchone()

        if row is None:
            return None

        return Object(

            id=row["id"],

            name=row["name"],

            source=row["source"] or "",

            external_id=row["external_id"] or "",

            address=row["address"] or "",

            customer=row["customer"] or "",

            contractor=row["contractor"] or "",

            designer=row["designer"] or "",

            manager=row["manager"] or "",

            status=row["status"] or "",

            comment=row["comment"] or ""

        )

    def save_objects(self, objects):

        saved = []

        for obj in objects:

            saved.append(
                self.save_object(obj)
            )

        return saved

    def load_objects(self):

        self.db.cursor.execute(
            """
            SELECT *

            FROM objects

            ORDER BY name
            """
        )

        rows = self.db.cursor.fetchall()

        objects = []

        for row in rows:

            objects.append(

                Object(

                    id=row["id"],

                    name=row["name"],

                    source=row["source"] or "",

                    external_id=row["external_id"] or "",

                    address=row["address"] or "",

                    customer=row["customer"] or "",

                    contractor=row["contractor"] or "",

                    designer=row["designer"] or "",

                    manager=row["manager"] or "",

                    status=row["status"] or "",

                    comment=row["comment"] or ""

                )

            )

        return objects