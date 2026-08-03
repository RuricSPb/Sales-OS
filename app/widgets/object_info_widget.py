from PySide6.QtWidgets import (
    QLabel,
    QFormLayout,
    QGroupBox,
    QTextEdit,
)


class ObjectInfoWidget(QGroupBox):

    def __init__(self):
        super().__init__("Общая информация")

        self.region = QLabel("")
        self.district = QLabel("")
        self.address = QLabel("")

        self.object_type = QLabel("")
        self.work_type = QLabel("")
        self.stage = QLabel("")
        self.frame_type = QLabel("")

        self.construction_period = QLabel("")
        self.visit_date = QLabel("")

        self.status = QLabel("")

        self.description = QTextEdit()
        self.description.setReadOnly(True)
        self.description.setMinimumHeight(120)

        self.comment = QTextEdit()
        self.comment.setReadOnly(True)
        self.comment.setMinimumHeight(80)

        form = QFormLayout()

        form.addRow("Регион:", self.region)
        form.addRow("Район:", self.district)
        form.addRow("Адрес:", self.address)

        form.addRow("Вид объекта:", self.object_type)
        form.addRow("Вид работ:", self.work_type)
        form.addRow("Этап:", self.stage)
        form.addRow("Каркас:", self.frame_type)

        form.addRow("Срок строительства:", self.construction_period)
        form.addRow("Дата посещения:", self.visit_date)

        form.addRow("Статус:", self.status)

        form.addRow("Описание:", self.description)

        form.addRow("Комментарий:", self.comment)

        self.setLayout(form)

    def show_object(self, obj):

        self.region.setText(obj.region)
        self.district.setText(obj.district)
        self.address.setText(obj.address)

        self.object_type.setText(obj.object_type)
        self.work_type.setText(obj.work_type)
        self.stage.setText(obj.stage)
        self.frame_type.setText(obj.frame_type)

        self.construction_period.setText(obj.construction_period)
        self.visit_date.setText(obj.visit_date)

        self.status.setText(obj.status)

        self.description.setPlainText(obj.description)

        self.comment.setPlainText(obj.comment)