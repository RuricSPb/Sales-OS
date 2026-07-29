from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QFormLayout,
    QVBoxLayout,
    QSizePolicy,
)


class Workspace(QWidget):

    def __init__(self):
        super().__init__()

        self.title = QLabel("Выберите объект")
        self.title.setWordWrap(True)
        self.title.setSizePolicy(
            QSizePolicy.Expanding,
            QSizePolicy.Minimum
        )
        self.address = QLabel("")
        self.customer = QLabel("")
        self.contractor = QLabel("")
        self.designer = QLabel("")
        self.manager = QLabel("")
        self.status = QLabel("")
        self.comment = QLabel("")

        self.title.setStyleSheet("""
            QLabel{
                font-size:24px;
                font-weight:bold;
                padding-bottom:15px;
            }
        """)

        form = QFormLayout()

        form.addRow("Адрес:", self.address)
        form.addRow("Заказчик:", self.customer)
        form.addRow("Генподрядчик:", self.contractor)
        form.addRow("Проектировщик:", self.designer)
        form.addRow("Менеджер:", self.manager)
        form.addRow("Статус:", self.status)
        form.addRow("Комментарий:", self.comment)

        layout = QVBoxLayout()

        layout.addWidget(self.title)
        layout.addLayout(form)
        layout.addStretch()

        self.setLayout(layout)

    def show_object(self, obj):

        self.title.setText(obj.name)

        self.address.setText(obj.address)
        self.customer.setText(obj.customer)
        self.contractor.setText(obj.contractor)
        self.designer.setText(obj.designer)
        self.manager.setText(obj.manager)
        self.status.setText(obj.status)
        self.comment.setText(obj.comment)