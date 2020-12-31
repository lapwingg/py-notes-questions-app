"""qpresentation_widget.py"""
from PyQt5.QtWidgets import QWidget, QPushButton, QLabel, QMessageBox, QHBoxLayout, \
    QVBoxLayout, QLineEdit, QPlainTextEdit, QListView, QAbstractItemView
from PyQt5.QtCore import Qt, QStringListModel
from PyQt5.QtGui import QShowEvent

from src.database.database import Database


class QPresentationWidget(QWidget):
    """Class which defines an application style, provides custom widgets for presentation area"""
    SmallButton = 0
    LargeButton = 1

    Notes = 2
    Questions = 3
    Technologies = 4

    show_event_method = None

    def __init__(self):
        super().__init__()
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setStyleSheet("background-color: rgba(0, 41, 59, 255)")
        self.layout = self.produce_vertical_layout()

    def set_layout(self):
        """Custom setLayout function"""
        self.setLayout(self.layout)

    @staticmethod
    def show_popup_with_text(text):
        """Show popup with text"""
        alert = QMessageBox()
        alert.setText(text)
        alert.exec_()

    @staticmethod
    def setup_background_color_for_widget(widget):
        """Setup app style background for widgets"""
        widget.setAttribute(Qt.WA_StyledBackground, True)
        widget.setStyleSheet("background-color: white;")

    def produce_button(self, text, size=SmallButton, on_clicked=None, enabled=True):
        """Produces button with text, custom size, on_clicked function, and enabled state or not"""
        button = QPushButton(text)
        if size == self.SmallButton:
            button.setFixedWidth(60)
        elif size == self.LargeButton:
            button.setFixedSize(100, 30)

        self.setup_background_color_for_widget(button)

        if on_clicked:
            button.clicked.connect(on_clicked)

        button.setEnabled(enabled)

        return button

    def produce_label(self, text):
        """Produces label with text"""
        label = QLabel(text)
        self.setup_background_color_for_widget(label)
        label.setContentsMargins(16, 0, 0, 0)
        return label

    @staticmethod
    def produce_widget():
        """Produces widget"""
        widget = QWidget()

        return widget

    @staticmethod
    def produce_horizontal_layout():
        """Produces horizontal layout"""
        return QHBoxLayout()

    @staticmethod
    def produce_vertical_layout():
        """Produces vertical layout"""
        return QVBoxLayout()

    def produce_line_edit(self, text):
        """Produces line edit with text"""
        line_edit = QLineEdit(text)
        self.setup_background_color_for_widget(line_edit)
        return line_edit

    def produce_plain_text_edit(self, plain_text):
        """Produces plain text edit with plain text"""
        plain_text = QPlainTextEdit(plain_text)
        self.setup_background_color_for_widget(plain_text)
        return plain_text

    def method_for_show_event(self, method):
        """Set method used by show event method"""
        self.show_event_method = method

    def showEvent(self, a0: QShowEvent) -> None:
        """Custom implementation of showEvent function"""
        if a0 == QShowEvent.Show:
            self.layout.removeWidget(self.list_view)
            self.show_event_method()
            self.setLayout(self.layout)

    def produce_list_view(self, data_type, on_clicked):
        """Produce list view depends of type"""
        list_view = QListView()
        database = Database()
        if data_type == self.Notes:
            notes = database.get_notes()
            list_view.setModel(QStringListModel(
                [note.name for note in notes]
            ))
        elif data_type == self.Questions:
            questions = database.get_questions()
            list_view.setModel(QStringListModel(
                [question.question for question in questions]
            ))
        elif data_type == self.Technologies:
            technologies = database.get_technologies()
            list_view.setModel(QStringListModel(
                [technology.name for technology in technologies]
            ))

        self.setup_background_color_for_widget(list_view)
        list_view.setEditTriggers(QAbstractItemView.NoEditTriggers)
        list_view.clicked.connect(on_clicked)
        return list_view
