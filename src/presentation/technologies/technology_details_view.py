"""technologies_details_view.py"""
from PyQt5.QtGui import QShowEvent

from src.database.database import Database
from src.presentation.qpresentation_widget import QPresentationWidget
from src.presentation.top_bar_producer import TopBarProducer


class TechnologyDetailsView(QPresentationWidget):
    """View representing a technology view"""
    name = ""
    technology = None

    def __init__(self, technology=None):
        super().__init__()
        if technology:
            self.technology = technology
            self.name = self.technology.name

        self.__setup_top_bar_buttons()
        self.__setup_edit_technology_layout()
        self.set_layout()

    def __setup_top_bar_buttons(self):
        back_button = self.produce_button('Back', on_clicked=self.__on_back_button_clicked)
        save_button = self.produce_button('Save', on_clicked=self.__on_save_button_clicked)
        top_bar_layout = TopBarProducer.produce_top_bar([back_button,
                                                         save_button])
        self.layout.addLayout(top_bar_layout)

    def __on_save_button_clicked(self):
        database = Database()
        if self.technology:
            database.update_technology(self.technology, self.edit_name.text())
        else:
            database.insert_technology(self.edit_name.text())

        self.__show_popup()
        self.__on_back_button_clicked()

    def __on_back_button_clicked(self):
        self.hide()
        self.parent().showEvent(QShowEvent.Show)

    def __show_popup(self):
        self.show_popup_with_text("Technology saved!")

    def __setup_edit_technology_layout(self):
        edit_technology_layout = self.produce_vertical_layout()
        self.edit_name = self.produce_line_edit(self.name)
        edit_technology_layout.addWidget(self.edit_name)
        widget = self.produce_widget()
        edit_technology_layout.addWidget(widget)
        self.layout.addLayout(edit_technology_layout)
