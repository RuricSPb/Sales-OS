from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QFileDialog,
    QMainWindow,
    QMessageBox,
    QSplitter,
    QStatusBar,
    QToolBar,
)

from app.object_list_v2 import ObjectListV2
from app.workspace import Workspace

from database.database import Database
from database.object_repository import ObjectRepository
from database.company_repository import CompanyRepository

from importers.psb_importer import PSBImporter

from services.object_service import ObjectService


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.database = Database()

        self.repository = ObjectRepository(self.database)
        self.company_repository = CompanyRepository(self.database)

        self.object_service = ObjectService(self.database)

        self.importer = PSBImporter()

        self.setWindowTitle("Sales OS")
        self.resize(1600, 900)

        self._create_menu()
        self._create_toolbar()
        self._create_statusbar()
        self._create_layout()

        self.load_saved_objects()

    # ---------------------------------------------------------

    def _create_menu(self):

        menu = self.menuBar()

        menu.addMenu("Файл")
        menu.addMenu("Объекты")
        menu.addMenu("КП")
        menu.addMenu("Аналитика")
        menu.addMenu("Настройки")
        menu.addMenu("Справка")

    # ---------------------------------------------------------

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

    # ---------------------------------------------------------

    def _create_statusbar(self):

        status = QStatusBar()

        status.showMessage("Готов к работе")

        self.setStatusBar(status)

    # ---------------------------------------------------------

    def _create_layout(self):

        splitter = QSplitter(Qt.Horizontal)

        self.object_list = ObjectListV2()

        self.workspace = Workspace()

        splitter.addWidget(self.object_list)
        splitter.addWidget(self.workspace)

        splitter.setSizes([320, 1280])

        self.setCentralWidget(splitter)

        self.object_list.selectionModel().currentChanged.connect(
            lambda current, previous: self.object_selected()
        )

    # ---------------------------------------------------------

    def load_saved_objects(self):

        objects = self.repository.load_objects()

        self.object_list.load_objects(objects)

        if objects:

            self.statusBar().showMessage(

                f"Загружено объектов: {len(objects)}"

            )

    # ---------------------------------------------------------

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

            imported = self.importer.import_objects(file_name)

            for item in imported.values():

                obj = item["object"]

                obj = self.repository.save_object(obj)

                companies = item["companies"]

                for company in companies:
                    company.object_id = obj.id

                self.company_repository.save_companies(companies)

            self.load_saved_objects()

            self.statusBar().showMessage(

                f"Импорт завершён"

            )

        except Exception as e:

            import traceback

            traceback.print_exc()

            QMessageBox.critical(

                self,

                "Ошибка импорта",

                str(e)

            )

    # ---------------------------------------------------------

    def object_selected(self):

        obj = self.object_list.get_current_object()

        if obj is None:
            return

        card = self.object_service.get_object_card(obj.id)

        self.workspace.show_object(card)