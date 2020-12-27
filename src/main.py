import sys

from src.MainWindow import MainWindow

from PyQt5.QtWidgets import QApplication


def main():
    py_app = QApplication([])
    view = MainWindow(resolution=QApplication.desktop().availableGeometry())
    view.show_()
    sys.exit(py_app.exec_())


if __name__ == '__main__':
    main()
