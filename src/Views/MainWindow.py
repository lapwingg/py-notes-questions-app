from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QHBoxLayout

from src.Views.Menu.MenuDrawer import MenuDrawer
from src.Views.Presentation.PresentationArea import PresentationArea

app_title = 'Py Notes / Questions App'


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle(app_title)
        self.setFixedSize(700, 700)
        self.generalLayout = self.install_first_class_views()
        self._centralWidget = QWidget(self)
        self.setCentralWidget(self._centralWidget)
        self._centralWidget.setLayout(self.generalLayout)

    @staticmethod
    def install_first_class_views():
        layout = QHBoxLayout()
        menu_drawer = MenuDrawer()
        layout.addWidget(menu_drawer)
        presentation_area = PresentationArea()
        layout.addWidget(presentation_area)
        return layout