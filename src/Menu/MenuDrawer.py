from PyQt5.QtWidgets import QWidget, QSizePolicy, QVBoxLayout, QListView, QAbstractItemView, QLabel
from PyQt5.QtCore import Qt, pyqtSignal


class MenuDrawer(QWidget):
    index_selected = pyqtSignal(int)

    def __init__(self, model):
        super().__init__()
        self.__setup_general_style()
        self.__setup_list_view(model)

    def __setup_general_style(self):
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setStyleSheet("background-color: white;")
        policy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        policy.setHorizontalStretch(2)
        self.setSizePolicy(policy)

    def __setup_list_view(self, model):
        box = QVBoxLayout(self)
        self.__setup_list_view_header(box)
        self.__setup_list_view_content(box, model)

    def __setup_list_view_header(self, layout):
        label = QLabel(text="Options")
        layout.addWidget(label)

    def __setup_list_view_content(self, layout, model):
        list_view = QListView()
        list_view.setModel(model)
        list_view.setEditTriggers(QAbstractItemView.NoEditTriggers)
        list_view.clicked.connect(self.__list_view_item_selected)
        layout.addWidget(list_view)

    def __list_view_item_selected(self, index):
        self.index_selected.emit(index.row())