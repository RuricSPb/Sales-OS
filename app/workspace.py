from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLabel, QVBoxLayout, QWidget


class Workspace(QWidget):

    def __init__(self):
        super().__init__()

        self.title = QLabel("Выберите объект")

        self.title.setAlignment(Qt.AlignTop)

        self.title.setStyleSheet("""
            QLabel {
                font-size: 26px;
                font-weight: bold;
                padding: 12px;
            }
        """)

        layout = QVBoxLayout()

        layout.addWidget(self.title)
        layout.addStretch()

        self.setLayout(layout)

    def show_object(self, obj):

        self.title.setText(obj.name)