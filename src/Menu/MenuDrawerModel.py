from PyQt5.QtCore import QStringListModel
from src.Presentation.Notes.NotesView import NotesView
from src.Presentation.Technologies.TechnologiesView import TechnologiesView
from src.Presentation.Questions.QuestionsView import QuestionsView
from src.Presentation.Quiz.QuizView import QuizView
from src.Presentation.Info.InfoView import InfoView


class MenuDrawerModel:
    @classmethod
    def model(cls):
        return QStringListModel(["Notes",
                                 "Technologies",
                                 "Questions",
                                 "Quiz",
                                 "Info"])

    @classmethod
    def view(cls, index):
        if index == 0:
            return NotesView()
        elif index == 1:
            return TechnologiesView()
        elif index == 2:
            return QuestionsView()
        elif index == 3:
            return QuizView()
        elif index == 4:
            return InfoView()
