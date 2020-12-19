import sys

from src.Views.MainWindow import MainWindow

from PyQt5.QtWidgets import QApplication

__version__ = '0.1'
__author__ = 'lapwingg'


def main():
    py_app = QApplication([])
    view = MainWindow(resolution=QApplication.desktop().availableGeometry())
    view.show_()
    sys.exit(py_app.exec_())


if __name__ == '__main__':
    main()
