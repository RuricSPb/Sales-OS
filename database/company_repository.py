from models.company import Company


class CompanyRepository:

    def __init__(self, database):

        self.db = database

    def save_company(self, company):

        self.db.cursor.execute(
            """
            INSERT INTO companies
            (
                object_id,
                company_name,
                company_type,
                contact,
                phone,
                email
            )

            VALUES
            (
                ?,?,?,?,?,?
            )
            """,
            (
                company.object_id,
                company.company_name,
                company.company_type,
                company.contact,
                company.phone,
                company.email
            )
        )

        self.db.connection.commit()

    def save_companies(self, companies):

        for company in companies:
            self.save_company(company)

    def get_companies(self, object_id):

        self.db.cursor.execute(
            """
            SELECT

                company_name,
                company_type,
                contact,
                phone,
                email

            FROM companies

            WHERE object_id = ?

            ORDER BY company_type
            """,
            (object_id,)
        )

        rows = self.db.cursor.fetchall()

        companies = []

        for row in rows:

            companies.append(

                Company(

                    object_id=object_id,

                    company_name=row[0],

                    company_type=row[1],

                    contact=row[2],

                    phone=row[3],

                    email=row[4]

                )

            )

        return companies