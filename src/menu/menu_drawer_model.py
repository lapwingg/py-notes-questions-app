"""menu_drawer_model.py"""
from PyQt5.QtCore import QStringListModel

from src.presentation.notes.notes_view import NotesView
from src.presentation.technologies.technologies_view import TechnologiesView
from src.presentation.questions.questions_view import QuestionsView
from src.presentation.quiz.quiz_view import QuizView
from src.presentation.info.info_view import InfoView


class MenuDrawerModel:
    """Menu helper object, storing model which is presenting into menu"""
    @classmethod
    def model(cls):
        """Returns available options in the menu"""
        return QStringListModel(["Notes",
                                 "Technologies",
                                 "Questions",
                                 "Quiz",
                                 "Info"])

    @classmethod
    def view(cls, index):
        """Returns a view respectively to the selected index in the menu"""
        view = None
        if index == 0:
            view = NotesView()
        elif index == 1:
            view = TechnologiesView()
        elif index == 2:
            view = QuestionsView()
        elif index == 3:
            view = QuizView()
        elif index == 4:
            view = InfoView()
        return view
