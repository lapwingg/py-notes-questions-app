from PyQt5.QtWidgets import QListView, QAbstractItemView
from PyQt5.QtCore import QStringListModel
from PyQt5.QtGui import QShowEvent

from src.Presentation.Technologies.TechnologyDetailsView import TechnologyDetailsView
from src.Presentation.QPresentationWidget import QPresentationWidget
from src.Database.Database import Database


class TechnologiesView(QPresentationWidget):
    def __init__(self):
        super().__init__()
        self.__setup_top_bar()
        self.__setup_technology_list_view()
        self.set_layout()

    def __setup_top_bar(self):
        top_bar = self.produce_horizontal_layout()
        separator = self.produce_widget()
        self.edit_technology_button = self.produce_button('Edit', on_clicked=self.__on_edit_button_clicked, enabled=False)
        self.remove_technology_button = self.produce_button('Remove', on_clicked=self.__on_remove_button_clicked, enabled=False)
        self.new_technology_button = self.produce_button('New', on_clicked=self.__on_new_button_clicked, enabled=True)
        self.filter_technology_button = self.produce_button('Filter', on_clicked=self.__show_popup, enabled=True)
        top_bar.addWidget(separator)
        top_bar.addWidget(self.edit_technology_button)
        top_bar.addWidget(self.remove_technology_button)
        top_bar.addWidget(self.new_technology_button)
        top_bar.addWidget(self.filter_technology_button)
        self.layout.addLayout(top_bar)

    def __on_edit_button_clicked(self):
        self.edit_technology_button.setEnabled(False)
        self.remove_technology_button.setEnabled(False)
        technology = self.technologies[self.selected_index]
        technology_details = TechnologyDetailsView(technology)
        technology_details.setParent(self)
        technology_details.setFixedWidth(self.width())
        technology_details.setFixedHeight(self.height())
        technology_details.show()

    def __on_remove_button_clicked(self):
        self.edit_technology_button.setEnabled(False)
        self.remove_technology_button.setEnabled(False)
        technology = self.technologies[self.selected_index]
        self.database.delete_technology(technology)
        self.showEvent(QShowEvent.Show)

    def __on_new_button_clicked(self):
        technology_details = TechnologyDetailsView()
        technology_details.setParent(self)
        technology_details.setFixedWidth(self.width())
        technology_details.setFixedHeight(self.height())
        technology_details.show()

    def __setup_technology_list_view(self):
        self.list_view = QListView()
        self.database = Database()
        self.technologies = self.database.get_technologies()
        self.list_view.setModel(QStringListModel([technology.name for technology in self.technologies]))
        self.setup_background_color_for_widget(self.list_view)
        self.list_view.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.list_view.clicked.connect(self.__list_view_item_selected)
        self.layout.addWidget(self.list_view)

    def __list_view_item_selected(self, index):
        self.edit_technology_button.setEnabled(True)
        self.remove_technology_button.setEnabled(True)
        self.selected_index = index.row()

    def __show_popup(self):
        self.show_popup_with_text("One day, you will be able to filter data!")

    def showEvent(self, a0: QShowEvent) -> None:
        if a0 == QShowEvent.Show:
            self.layout.removeWidget(self.list_view)
            self.__setup_technology_list_view()
            self.setLayout(self.layout)
