"""main.py"""
import sys

from PyQt5.QtWidgets import QApplication

from src.main_window import MainWindow
from src.database.database import Database


def main():
    """Actions to do when the application starts"""
    py_app = QApplication([])
    Database()
    view = MainWindow(resolution=QApplication.desktop().availableGeometry())
    view.show_()
    sys.exit(py_app.exec_())


if __name__ == '__main__':
    main()
