from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import (
    QColor,
    QFont,
    QPainter,
    QPen,
)
from PySide6.QtWidgets import (
    QStyledItemDelegate,
    QStyle,
)


class ObjectItemDelegate(QStyledItemDelegate):

    def sizeHint(self, option, index):

        return QSize(300, 74)

    # ---------------------------------------------------------

    def paint(self, painter, option, index):

        obj = index.data(Qt.UserRole)

        if obj is None:
            return

        painter.save()

        rect = option.rect

        # ---------- фон ----------

        if option.state & QStyle.State_Selected:

            painter.fillRect(
                rect,
                QColor("#dbeafe")
            )

        else:

            painter.fillRect(
                rect,
                QColor("white")
            )

        # ---------- нижняя линия ----------

        painter.setPen(
            QPen(QColor("#dddddd"))
        )

        painter.drawLine(
            rect.bottomLeft(),
            rect.bottomRight()
        )

        # ---------- название ----------

        font = QFont("Segoe UI", 10)
        font.setBold(True)

        painter.setFont(font)
        painter.setPen(QColor("#202020"))

        painter.drawText(

            rect.adjusted(
                12,
                8,
                -12,
                -30
            ),

            Qt.AlignLeft | Qt.TextWordWrap,

            obj.name

        )

        # ---------- адрес ----------

        address = getattr(obj, "address", "")

        if address:

            painter.setFont(
                QFont("Segoe UI", 9)
            )

            painter.setPen(
                QColor("#666666")
            )

            painter.drawText(

                rect.adjusted(
                    12,
                    42,
                    -12,
                    -6
                ),

                Qt.AlignLeft | Qt.TextWordWrap,

                address

            )

        painter.restore()