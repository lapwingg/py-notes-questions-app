"""info_view.py"""
from src.presentation.info.info_view_model import InfoViewModel
from src.presentation.qpresentation_widget import QPresentationWidget


class InfoView(QPresentationWidget):
    """View representing Info option in the presentation area"""
    def __init__(self):
        super().__init__()
        self.__setup_top_bar()
        self.__setup_app_info_bar()
        self.__setup_content_info_bar()
        self.set_layout()

    def __setup_top_bar(self):
        top_bar = self.produce_horizontal_layout()
        separator_widget = self.produce_widget()
        top_bar.addWidget(separator_widget)
        send_opinion_button = self.produce_button("Send Opinion",
                                                  size=self.LargeButton,
                                                  on_clicked=self.__show_popup)
        top_bar.addWidget(send_opinion_button)
        self.layout.addLayout(top_bar)

    def __setup_app_info_bar(self):
        app_bar_widget = self.produce_widget()
        app_bar = self.produce_vertical_layout()
        developer_info = self.produce_label(f'Developer: {InfoViewModel.developer}')
        app_bar.addWidget(developer_info)
        version_info = self.produce_label(f'Version: {InfoViewModel.app_version}')
        app_bar.addWidget(version_info)
        commit_hash = self.produce_label(f'Commit: {InfoViewModel.commit_hash}')
        app_bar.addWidget(commit_hash)
        py_qt_version = self.produce_label(f'PyQt {InfoViewModel.py_qt_version}')
        app_bar.addWidget(py_qt_version)
        python_version = self.produce_label(f'Python {InfoViewModel.python_version}')
        app_bar.addWidget(python_version)
        app_bar_widget.setLayout(app_bar)
        self.layout.addWidget(app_bar_widget)

    def __setup_content_info_bar(self):
        content_info_bar_widget = self.produce_widget()
        content_info_bar = self.produce_vertical_layout()
        notes_count = self.produce_label(f'Notes: {InfoViewModel.notes_count()}')
        content_info_bar.addWidget(notes_count)
        technologies_count = self.produce_label(
            f'Technologies: {InfoViewModel.technologies_count()}'
        )
        content_info_bar.addWidget(technologies_count)
        questions_count = self.produce_label(f'Questions: {InfoViewModel.questions_count()}')
        content_info_bar.addWidget(questions_count)
        content_info_bar_widget.setLayout(content_info_bar)
        self.layout.addWidget(content_info_bar_widget)

    def __show_popup(self):
        self.show_popup_with_text("One day, you will be able to submit your opinion!")
