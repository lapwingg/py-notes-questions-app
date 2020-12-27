from PyQt5.QtWidgets import QMainWindow, QWidget, QHBoxLayout
from PyQt5.QtCore import Qt

from src.Menu.MenuDrawer import MenuDrawer
from src.Presentation.PresentationArea import PresentationArea
from src.Menu.MenuDrawerModel import MenuDrawerModel

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
        self.setAttribute(Qt.WA_StyledBackground, True)
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

    def __setup_general_layout(self):
        layout = QHBoxLayout()
        model = MenuDrawerModel.model()
        self.menu_drawer = MenuDrawer(model)
        self.menu_drawer.index_selected.connect(self.present_view_for_index_selected)
        layout.addWidget(self.menu_drawer)
        self.presentation_area = PresentationArea()
        layout.addWidget(self.presentation_area)
        return layout

    def present_view_for_index_selected(self, index):
        self.presentation_area.change_widget(MenuDrawerModel.view(index))