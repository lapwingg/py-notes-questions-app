from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QMessageBox
from PyQt5.QtCore import Qt

from src.Presentation.Info.InfoViewModel import InfoViewModel


class InfoView(QWidget):
    def __init__(self):
        super().__init__()
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setStyleSheet("background-color: rgba(0, 41, 59, 255)")
        self.general_layout = QVBoxLayout()
        self.__setup_top_bar()
        self.__setup_app_info_bar()
        self.__setup_content_info_bar()
        self.setLayout(self.general_layout)

    def __setup_top_bar(self):
        top_bar = QHBoxLayout()
        separator_widget = QWidget()
        top_bar.addWidget(separator_widget)
        send_opinion_button = QPushButton("Send opinion!")
        send_opinion_button.setFixedSize(100, 30)
        self.__setup_attribute(send_opinion_button)
        send_opinion_button.clicked.connect(self.__show_popup)
        top_bar.addWidget(send_opinion_button)
        self.general_layout.addLayout(top_bar)

    def __setup_app_info_bar(self):
        app_bar_widget = QWidget()
        app_bar = QVBoxLayout()
        developer_info = self.__prepare_label(f'Developer: {InfoViewModel.developer}')
        app_bar.addWidget(developer_info)
        version_info = self.__prepare_label(f'Version: {InfoViewModel.app_version}')
        app_bar.addWidget(version_info)
        commit_hash = self.__prepare_label(f'Commit: {InfoViewModel.commit_hash}')
        app_bar.addWidget(commit_hash)
        py_qt_version = self.__prepare_label(f'PyQt {InfoViewModel.py_qt_version}')
        app_bar.addWidget(py_qt_version)
        python_version = self.__prepare_label(f'Python {InfoViewModel.python_version}')
        app_bar.addWidget(python_version)
        app_bar_widget.setLayout(app_bar)
        self.general_layout.addWidget(app_bar_widget)

    def __setup_content_info_bar(self):
        content_info_bar_widget = QWidget()
        content_info_bar = QVBoxLayout()
        notes_count = self.__prepare_label(f'Notes: {InfoViewModel.notes_count()}')
        content_info_bar.addWidget(notes_count)
        technologies_count = self.__prepare_label(f'Technologies: {InfoViewModel.technologies_count()}')
        content_info_bar.addWidget(technologies_count)
        questions_count = self.__prepare_label(f'Questions: {InfoViewModel.questions_count()}')
        content_info_bar.addWidget(questions_count)
        content_info_bar_widget.setLayout(content_info_bar)
        self.general_layout.addWidget(content_info_bar_widget)

    def __prepare_label(self, text):
        label = QLabel(text)
        self.__setup_attribute(label)
        label.setContentsMargins(16, 0, 0, 0)
        return label

    def __setup_attribute(self, widget):
        widget.setAttribute(Qt.WA_StyledBackground, True)
        widget.setStyleSheet("background-color: white;")

    def __show_popup(self):
        alert = QMessageBox()
        alert.setText("One day, you will be able to submit your opinion!")
        alert.exec_()
