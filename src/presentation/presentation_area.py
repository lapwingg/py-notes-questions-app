"""presentation_area.py"""
from PyQt5.QtWidgets import QWidget, QSizePolicy, QVBoxLayout


class PresentationArea(QWidget):
    """View representing an area when are showed selected option, root for this action"""

    current_widget = None

    def __init__(self, widget=None):
        super().__init__()
        self.__setup_size_policy()
        self.__setup_general_layout()
        self.__setup_init_widget(widget=widget)

    def __setup_size_policy(self):
        policy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        policy.setHorizontalStretch(5)
        self.setSizePolicy(policy)

    def __setup_general_layout(self):
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

    def __setup_init_widget(self, widget=None):
        if widget:
            self.current_widget = widget
            self.layout.addWidget(widget)
        else:
            self.current_widget = None

    def change_widget(self, new_widget):
        """Changes current presented widget in the presentation area"""
        if self.current_widget:
            self.layout.replaceWidget(self.current_widget, new_widget)
        else:
            self.layout.addWidget(new_widget)

        self.current_widget = new_widget
