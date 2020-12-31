"""main_window.py"""
from PyQt5.QtWidgets import QMainWindow, QWidget, QHBoxLayout
from PyQt5.QtCore import Qt

from src.menu.menu_drawer import MenuDrawer
from src.presentation.presentation_area import PresentationArea
from src.menu.menu_drawer_model import MenuDrawerModel

APP_TITLE = 'Py notes / questions App'
MIN_WIDTH = 100
MIN_HEIGHT = 100


class MainWindow(QMainWindow):
    """Definion of first loaded view in the app"""

    def __init__(self, resolution=None):
        super().__init__()
        self.setWindowTitle(APP_TITLE)
        self.__calculate_window_size(resolution=resolution)
        self.general_layout = self.__setup_general_layout()
        self._central_widget = QWidget(self)
        self.setCentralWidget(self._central_widget)
        self._central_widget.setLayout(self.general_layout)
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setStyleSheet("background-color: rgba(0, 41, 59, 255)")
        self.show_(resolution=resolution)

    def show_(self, resolution=None):
        """Override show function, presentation depends on screen resolution"""
        self.show()
        if resolution:
            self.move(resolution.center() - self.rect().center())

    def __calculate_window_size(self, resolution=None):
        if resolution:
            self.setMinimumWidth(resolution.width() / 3)
            self.setMinimumHeight(resolution.height() / 1.5)
        else:
            self.setMinimumWidth(MIN_WIDTH)
            self.setMinimumHeight(MIN_HEIGHT)

    def __setup_general_layout(self):
        layout = QHBoxLayout()
        model = MenuDrawerModel.model()
        self.menu_drawer = MenuDrawer(model)
        self.menu_drawer.index_selected.connect(self.__present_view_for_index_selected)
        layout.addWidget(self.menu_drawer)
        self.presentation_area = PresentationArea()
        layout.addWidget(self.presentation_area)
        return layout

    def __present_view_for_index_selected(self, index):
        self.presentation_area.change_widget(MenuDrawerModel.view(index))
