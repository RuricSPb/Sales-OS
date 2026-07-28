from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLabel, QVBoxLayout, QWidget


class Workspace(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)

        title = QLabel("Sales OS")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("""
            font-size:28px;
            font-weight:bold;
        """)

        info = QLabel(
            "Рабочая область\n\n"
            "Следующий этап — импорт отчёта ПСБ."
        )
        info.setAlignment(Qt.AlignCenter)

        layout.addStretch()
        layout.addWidget(title)
        layout.addWidget(info)
        layout.addStretch()