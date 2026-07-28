from PySide6.QtWidgets import QListWidget


class ObjectList(QListWidget):

    def __init__(self):
        super().__init__()

    def load_objects(self, objects):

        self.clear()

        for obj in objects:
            self.addItem(obj.name)