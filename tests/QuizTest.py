import unittest
import os

from src.Database.Database import Database
from src.Presentation.Quiz.QuizViewModel import QuizViewModel


class QuizTest(unittest.TestCase):
    database_name = "project_test.db"
    expected_result = ""
    expected_question = ""
    expected_answer = ""

    def current_result_checker(self, result):
        self.assertEqual(result == self.expected_result, True)

    def current_question_checker(self, question):
        self.assertEqual(question == self.expected_question, True)

    def current_answer_checker(self, answer):
        self.assertEqual(answer == self.expected_answer, True)

    def test(self):
        # prepare database
        database = Database(database_name=self.database_name)
        for i in range(0, 5):
            database.insert_question(f"A_{i}", f"B_{i}")

        # setup object
        sut = QuizViewModel(database_name=self.database_name)
        sut.current_result.connect(self.current_result_checker)
        sut.question.connect(self.current_question_checker)
        sut.answer.connect(self.current_answer_checker)

        # scenario
        self.expected_result = "0 / 0"
        self.expected_question = "A_0"
        sut.on_start()

        self.expected_answer = "B_0"
        sut.answer_for_question()

        self.expected_result = "0 / 1"
        sut.was_incorrect_answer()

        self.expected_question = "A_1"
        sut.next_question()

        self.expected_answer = "B_1"
        sut.answer_for_question()

        self.expected_result = "1 / 2"
        sut.was_correct_answer()

        self.expected_question = "A_2"
        sut.next_question()

        self.expected_answer = "B_2"
        sut.answer_for_question()

        self.expected_result = "2 / 3"
        sut.was_correct_answer()

        self.expected_question = "A_3"
        sut.next_question()

        self.expected_answer = "B_3"
        sut.answer_for_question()

        self.expected_result = "2 / 4"
        sut.was_incorrect_answer()

        self.expected_question = "A_4"
        sut.next_question()

        self.expected_answer = "B_4"
        sut.answer_for_question()

        self.expected_result = "2 / 5"
        sut.was_incorrect_answer()

        self.expected_question = ""
        sut.next_question()

        self.expected_question = ""
        for i in range(0, 10):
            sut.next_question()

        self.expected_result = "0 / 0"
        self.expected_question = "A_0"
        sut.on_start()

        # drop database
        os.remove(self.database_name)
