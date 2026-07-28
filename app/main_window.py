from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QFileDialog,
    QMainWindow,
    QMessageBox,
    QSplitter,
    QStatusBar,
    QToolBar,
)

from app.object_list import ObjectList
from app.workspace import Workspace
from importers.psb_importer import PSBImporter


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.importer = PSBImporter()

        self.setWindowTitle("Sales OS")
        self.resize(1600, 900)

        self._create_menu()
        self._create_toolbar()
        self._create_statusbar()
        self._create_layout()

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

        toolbar.addAction("Новый объект")

        toolbar.addSeparator()

        action_import = toolbar.addAction("Импорт ПСБ")
        action_import.triggered.connect(self.import_psb)

        toolbar.addSeparator()

        toolbar.addAction("Обновить")

        self.addToolBar(toolbar)

    def _create_statusbar(self):

        status = QStatusBar()
        status.showMessage("Готов к работе")

        self.setStatusBar(status)

    def _create_layout(self):

        splitter = QSplitter(Qt.Horizontal)

        self.object_list = ObjectList()

        splitter.addWidget(self.object_list)
        splitter.addWidget(Workspace())

        splitter.setSizes([320, 1280])

        self.setCentralWidget(splitter)

    def import_psb(self):

        file_name, _ = QFileDialog.getOpenFileName(
            self,
            "Выберите отчёт ПСБ",
            "",
            "Excel (*.xlsx)"
        )

        if not file_name:
            return

        try:

            objects = self.importer.import_objects(file_name)

            self.object_list.load_objects(objects)

            self.statusBar().showMessage(
                f"Импортировано объектов: {len(objects)}"
            )

        except Exception as e:

            QMessageBox.critical(
                self,
                "Ошибка импорта",
                str(e)
            )