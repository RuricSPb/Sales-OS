from openpyxl import load_workbook

from models.object import Object
from models.company import Company


class PSBImporter:

    def import_objects(self, filename):

        workbook = load_workbook(filename=filename)

        sheet = workbook.active

        headers = {}

        for col in range(1, sheet.max_column + 1):

            value = sheet.cell(row=1, column=col).value

            if value:

                headers[str(value).strip()] = col

        objects = {}

        for row in range(2, sheet.max_row + 1):

            object_name = self._cell(
                sheet,
                row,
                headers,
                "Объект"
            )

            if not object_name:
                continue

            if object_name not in objects:

                obj = Object(

                    name=object_name,

                    source="ПСБ"

                )

                objects[object_name] = {

                    "object": obj,

                    "companies": []

                }

            company = Company(

                company_name=self._cell(
                    sheet,
                    row,
                    headers,
                    "Название компании-участника строительства"
                ),

                company_type=self._cell(
                    sheet,
                    row,
                    headers,
                    "Тип компании"
                ),

                contact=self._cell(
                    sheet,
                    row,
                    headers,
                    "Контакт компании"
                ),

                phone=self._cell(
                    sheet,
                    row,
                    headers,
                    "Тел. компании"
                ),

                email=self._cell(
                    sheet,
                    row,
                    headers,
                    "E-mail компании"
                )

            )

            objects[object_name]["companies"].append(company)

        return objects

    def _cell(self, sheet, row, headers, header):

        column = headers.get(header)

        if column is None:
            return ""

        value = sheet.cell(row=row, column=column).value

        if value is None:
            return ""

        return str(value).strip()