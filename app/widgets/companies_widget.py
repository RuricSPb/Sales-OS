from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QFormLayout,
    QGroupBox,
)


class CompaniesWidget(QGroupBox):

    def __init__(self):
        super().__init__("Участники строительства")

        self.customer = QLabel("")
        self.contractor = QLabel("")
        self.designer = QLabel("")

        form = QFormLayout()

        form.addRow("Заказчик:", self.customer)
        form.addRow("Генподрядчик:", self.contractor)
        form.addRow("Проектировщик:", self.designer)

        self.setLayout(form)

    def show_card(self, card):

        self.customer.setText(
            card.customer.company_name
            if card.customer else ""
        )

        self.contractor.setText(
            card.contractor.company_name
            if card.contractor else ""
        )

        self.designer.setText(
            card.designer.company_name
            if card.designer else ""
        )