from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QVBoxLayout,
    QSizePolicy,
)

from app.widgets.object_info_widget import ObjectInfoWidget
from app.widgets.companies_widget import CompaniesWidget


class Workspace(QWidget):

    def __init__(self):
        super().__init__()

        # ---------- Заголовок ----------

        self.title = QLabel("Выберите объект")

        self.title.setWordWrap(True)

        self.title.setSizePolicy(
            QSizePolicy.Expanding,
            QSizePolicy.Minimum
        )

        self.title.setStyleSheet("""
            QLabel{
                font-size:24px;
                font-weight:bold;
            }
        """)

        # ---------- Виджеты ----------

        self.object_info = ObjectInfoWidget()

        self.companies = CompaniesWidget()

        # ---------- Layout ----------

        layout = QVBoxLayout()

        layout.addWidget(self.title)

        layout.addSpacing(15)

        layout.addWidget(self.object_info)

        layout.addWidget(self.companies)

        layout.addStretch()

        self.setLayout(layout)

    def show_object(self, card):

        if card is None:
            return

        self.title.setText(card.object.name)

        self.object_info.show_object(card.object)

        self.companies.show_card(card)