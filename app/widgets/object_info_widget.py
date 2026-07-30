from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QFormLayout,
    QGroupBox,
)


class ObjectInfoWidget(QGroupBox):

    def __init__(self):
        super().__init__("Общая информация")

        self.address = QLabel("")
        self.status = QLabel("")
        self.manager = QLabel("")
        self.comment = QLabel("")

        form = QFormLayout()

        form.addRow("Адрес:", self.address)
        form.addRow("Статус:", self.status)
        form.addRow("Менеджер:", self.manager)
        form.addRow("Комментарий:", self.comment)

        self.setLayout(form)

    def show_object(self, obj):

        self.address.setText(obj.address)
        self.status.setText(obj.status)
        self.manager.setText(obj.manager)
        self.comment.setText(obj.comment)