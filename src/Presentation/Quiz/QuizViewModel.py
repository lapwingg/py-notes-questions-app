from PyQt5.QtCore import pyqtSignal, QObject

from src.Database.Database import Database


class QuizViewModel(QObject):
    __questions = []
    __current_question_index = -1
    __correct_answers = 0
    __questions_given = 0
    __database_name = "project.db"

    current_result = pyqtSignal(str)
    question = pyqtSignal(str)
    answer = pyqtSignal(str)

    def __init__(self, database_name=None):
        super().__init__()
        if database_name:
            self.__database_name = database_name

    def on_start(self):
        self.__clear()
        self.__emit_current_result()
        self.next_question()

    def next_question(self):
        self.__current_question_index += 1
        if self.__current_question_index < len(self.__questions):
            self.__questions_given += 1
            self.question.emit(self.__questions[self.__current_question_index].question)
        else:
            self.question.emit("")

    def answer_for_question(self):
        self.answer.emit(self.__questions[self.__current_question_index].answer)

    def was_incorrect_answer(self):
        self.__emit_current_result()

    def was_correct_answer(self):
        self.__correct_answers += 1
        self.__emit_current_result()

    def __emit_current_result(self):
        self.current_result.emit(f"{self.__correct_answers} / {self.__questions_given}")

    def __clear(self):
        database = Database(database_name=self.__database_name)
        self.__questions = database.get_questions()
        self.__current_question_index = -1
        self.__correct_answers = 0
        self.__questions_given = 0
