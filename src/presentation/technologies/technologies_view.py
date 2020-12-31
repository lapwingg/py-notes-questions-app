"""technologies_view.py"""
from PyQt5.QtGui import QShowEvent

from src.presentation.technologies.technology_details_view import TechnologyDetailsView
from src.presentation.qpresentation_widget import QPresentationWidget
from src.database.database import Database
from src.presentation.top_bar_producer import TopBarProducer


class TechnologiesView(QPresentationWidget):
    """View presenting technology stored in the database"""

    selected_index = None

    def __init__(self):
        super().__init__()
        self.method_for_show_event(self.__setup_technologies_list_view)
        self.__setup_top_bar()
        self.__setup_technologies_list_view()
        self.set_layout()

    def __setup_top_bar(self):
        self.edit_technology_button = self.produce_button('Edit',
                                                          on_clicked=self.__on_edit_button_c,
                                                          enabled=False)
        self.remove_technology_button = self.produce_button('Remove',
                                                            on_clicked=self.__on_remove_button_c,
                                                            enabled=False)
        new_technology_button = self.produce_button('New',
                                                    on_clicked=self.__on_new_button_c,
                                                    enabled=True)
        self.filter_technology_button = self.produce_button('Filter',
                                                            on_clicked=self.__show_popup,
                                                            enabled=True)
        top_bar = TopBarProducer.produce_top_bar([self.edit_technology_button,
                                                  self.remove_technology_button,
                                                  new_technology_button,
                                                  self.filter_technology_button])
        self.layout.addLayout(top_bar)

    def __on_edit_button_c(self):
        self.edit_technology_button.setEnabled(False)
        self.remove_technology_button.setEnabled(False)
        technology = self.technologies[self.selected_index]
        technology_details = TechnologyDetailsView(technology)
        technology_details.setParent(self)
        technology_details.setFixedWidth(self.width())
        technology_details.setFixedHeight(self.height())
        technology_details.show()

    def __on_remove_button_c(self):
        self.edit_technology_button.setEnabled(False)
        self.remove_technology_button.setEnabled(False)
        technology = self.technologies[self.selected_index]
        self.database.delete_technology(technology)
        self.showEvent(QShowEvent.Show)

    def __on_new_button_c(self):
        technology_details = TechnologyDetailsView()
        technology_details.setParent(self)
        technology_details.setFixedWidth(self.width())
        technology_details.setFixedHeight(self.height())
        technology_details.show()

    def __setup_technologies_list_view(self):
        self.list_view = self.produce_list_view(data_type=self.Technologies,
                                                on_clicked=self.__list_view_item_selected)
        self.database = Database()
        self.technologies = self.database.get_technologies()
        self.layout.addWidget(self.list_view)

    def __list_view_item_selected(self, index):
        self.edit_technology_button.setEnabled(True)
        self.remove_technology_button.setEnabled(True)
        self.selected_index = index.row()

    def __show_popup(self):
        self.show_popup_with_text("One day, you will be able to filter data!")
