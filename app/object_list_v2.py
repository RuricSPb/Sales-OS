from PySide6.QtCore import Qt
from PySide6.QtGui import (
    QStandardItem,
    QStandardItemModel,
)
from PySide6.QtWidgets import QListView

from app.object_item_delegate import ObjectItemDelegate


class ObjectListV2(QListView):

    def __init__(self):
        super().__init__()

        self.model = QStandardItemModel()

        self.setModel(self.model)

        self.setItemDelegate(
            ObjectItemDelegate()
        )

        self.setSelectionMode(
            QListView.SingleSelection
        )

        self.setEditTriggers(
            QListView.NoEditTriggers
        )

        self.setVerticalScrollMode(
            QListView.ScrollPerPixel
        )

        self.setHorizontalScrollBarPolicy(
            Qt.ScrollBarAlwaysOff
        )

        self.setSpacing(2)

        self.setUniformItemSizes(False)

    # -----------------------------------------------------

    def load_objects(self, objects):

        self.model.clear()

        for obj in objects:

            item = QStandardItem()

            #
            # ВАЖНО:
            # сохраняем объект в UserRole
            #

            item.setData(
                obj,
                Qt.UserRole
            )

            item.setEditable(False)

            self.model.appendRow(item)

    # -----------------------------------------------------

    def get_current_object(self):

        index = self.currentIndex()

        if not index.isValid():
            return None

        return index.data(Qt.UserRole)