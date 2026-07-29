from PySide6.QtWidgets import QListWidget


class ObjectList(QListWidget):

    def __init__(self):
        super().__init__()

        self.objects = []

    def load_objects(self, objects):

        self.clear()

        self.objects = objects

        for obj in objects:
            self.addItem(obj.name)

    def get_current_object(self):

        row = self.currentRow()

        if row < 0:
            return None

        return self.objects[row]