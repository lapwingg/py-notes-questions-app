from PyQt5.QtCore import QStringListModel


class MenuDrawerModel:
    @classmethod
    def model(cls):
        return QStringListModel(["Notes",
                                 "Technologies",
                                 "Questions",
                                 "Quizzes",
                                 "Info"])