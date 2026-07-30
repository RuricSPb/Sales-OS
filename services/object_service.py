from database.object_repository import ObjectRepository
from database.company_repository import CompanyRepository

from models.object_card import ObjectCard


class ObjectService:

    def __init__(self, database):

        self.object_repository = ObjectRepository(database)
        self.company_repository = CompanyRepository(database)

    def get_object_card(self, object_id):

        obj = self.object_repository.get_object(object_id)

        if obj is None:
            return None

        card = ObjectCard(obj)

        companies = self.company_repository.get_companies(object_id)

        for company in companies:

            company_type = (company.company_type or "").lower()

            if (
                "заказ" in company_type
                or "застрой" in company_type
            ):
                card.customer = company

            elif "ген" in company_type:
                card.contractor = company

            elif "проект" in company_type:
                card.designer = company

        return card