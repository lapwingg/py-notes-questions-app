from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QHBoxLayout
import PyQt5.QtCore as QtCore

from src.Views.Menu.MenuDrawer import MenuDrawer
from src.Views.Presentation.PresentationArea import PresentationArea

app_title = 'Py Notes / Questions App'
min_width = 100
min_height = 100


class MainWindow(QMainWindow):
    def __init__(self, resolution=None):
        super().__init__()
        self.setWindowTitle(app_title)
        self.__calculate_window_size(resolution=resolution)
        self.generalLayout = self.__setup_general_layout()
        self._centralWidget = QWidget(self)
        self.setCentralWidget(self._centralWidget)
        self._centralWidget.setLayout(self.generalLayout)
        self.setAttribute(QtCore.Qt.WA_StyledBackground, True)
        self.setStyleSheet("background-color: rgba(0, 41, 59, 255)")
        self.show_(resolution=resolution)

    def show_(self, resolution=None):
        self.show()
        if resolution:
            self.move(resolution.center() - self.rect().center())

    def __calculate_window_size(self, resolution=None):
        if resolution:
            self.setMinimumWidth(resolution.width() / 3)
            self.setMinimumHeight(resolution.height() / 1.5)
        else:
            self.setMinimumWidth(min_width)
            self.setMinimumHeight(min_height)

    @staticmethod
    def __setup_general_layout():
        layout = QHBoxLayout()
        menu_drawer = MenuDrawer()
        layout.addWidget(menu_drawer)
        presentation_area = PresentationArea()
        layout.addWidget(presentation_area)
        return layout
