from pathlib import Path

from openpyxl import load_workbook

from models.object import Object


class PSBImporter:

    def import_objects(self, file_path):

        file_path = Path(file_path)

        workbook = load_workbook(file_path, data_only=True)

        sheet = workbook["ПетроСтройБаза"]

        headers = {}

        for col in range(1, sheet.max_column + 1):
            value = sheet.cell(row=1, column=col).value

            if value is not None:
                headers[str(value).strip()] = col

        if "Объект" not in headers:
            raise Exception("Столбец 'Объект' не найден.")

        object_column = headers["Объект"]

        objects = {}
        
        for row in range(2, sheet.max_row + 1):

            value = sheet.cell(row=row, column=object_column).value

            if value is None:
                continue

            name = str(value).strip()

            if not name:
                continue

            if name not in objects:
                objects[name] = Object(name=name)

        return sorted(objects.values(), key=lambda x: x.name)