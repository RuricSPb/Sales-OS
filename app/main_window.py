from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QMainWindow,
    QLabel,
    QStatusBar,
    QToolBar,
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Sales OS v0.2.0")
        self.resize(1400, 900)

        self._create_menu()
        self._create_toolbar()
        self._create_statusbar()
        self._create_central_widget()

    def _create_menu(self):
        menu = self.menuBar()

        menu.addMenu("Файл")
        menu.addMenu("Объекты")
        menu.addMenu("КП")
        menu.addMenu("Аналитика")
        menu.addMenu("Настройки")
        menu.addMenu("Справка")

    def _create_toolbar(self):
        toolbar = QToolBar("Основная панель")
        toolbar.setMovable(False)
        self.addToolBar(toolbar)

    def _create_statusbar(self):
        status = QStatusBar()
        status.showMessage("Готов к работе")
        self.setStatusBar(status)

    def _create_central_widget(self):
        label = QLabel("Sales OS\n\nВерсия 0.2.0")
        label.setAlignment(Qt.AlignCenter)
        label.setStyleSheet("""
            QLabel {
                font-size: 28px;
            }
        """)
        self.setCentralWidget(label)