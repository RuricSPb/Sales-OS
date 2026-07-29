from database.object_repository import ObjectRepository
from database.company_repository import CompanyRepository


class ObjectService:

    def __init__(self, database):

        self.object_repository = ObjectRepository(database)
        self.company_repository = CompanyRepository(database)

    def get_object_card(self, object_id):

        print("\n==============================")
        print("ObjectService")
        print("==============================")
        print(f"object_id = {object_id}")

        obj = self.object_repository.get_object(object_id)

        if obj is None:
            print("Объект НЕ найден!")
            return None

        print(f"Object = {obj.name}")

        companies = self.company_repository.get_companies(object_id)

        print(f"Companies found = {len(companies)}")

        for company in companies:

            print(
                f"{company.company_type} --> {company.company_name}"
            )

            company_type = (company.company_type or "").lower()

            if (
                "заказ" in company_type
                or "застрой" in company_type
            ):
                obj.customer = company.company_name

            elif "ген" in company_type:
                obj.contractor = company.company_name

            elif "проект" in company_type:
                obj.designer = company.company_name

        print("------------------------------")
        print(f"Customer   = {obj.customer}")
        print(f"Contractor = {obj.contractor}")
        print(f"Designer   = {obj.designer}")
        print("==============================\n")

        return obj