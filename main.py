import sys

from PySide6.QtWidgets import QApplication

from app.main_window import MainWindow


def load_style(app):

    try:
        with open("resources/style.qss", "r", encoding="utf-8") as f:
            app.setStyleSheet(f.read())

    except FileNotFoundError:
        print("Файл style.qss не найден.")


def main():

    app = QApplication(sys.argv)

    load_style(app)

    window = MainWindow()

    window.showMaximized()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()