import unittest
import os
from src.database.database import Database


class DatabaseTest(unittest.TestCase):
    database_name = "project_test.db"

    def test(self):
        self.assertEqual(os.path.exists(DatabaseTest.database_name), False)

        # creation - should be empty
        sut = Database(database_name=DatabaseTest.database_name)
        self.assertEqual(sut.get_notes(), [])
        self.assertEqual(sut.get_technologies(), [])
        self.assertEqual(sut.get_questions(), [])

        # insert one note
        sut.insert_note("A", "BBBB")
        notes = sut.get_notes()
        self.assertEqual(len(notes), 1)
        self.assertEqual(notes[0].id_value, 1)
        self.assertEqual(notes[0].name, "A")
        self.assertEqual(notes[0].description, "BBBB")

        # insert one technology
        sut.insert_technology("B")
        technologies = sut.get_technologies()
        self.assertEqual(len(technologies), 1)
        self.assertEqual(technologies[0].id_value, 1)
        self.assertEqual(technologies[0].name, "B")

        # insert one question
        sut.insert_question("A?", "B")
        questions = sut.get_questions()
        self.assertEqual(len(questions), 1)
        self.assertEqual(questions[0].id_value, 1)
        self.assertEqual(questions[0].question, "A?")
        self.assertEqual(questions[0].answer, "B")

        # insert some notes
        for i in range(0, 5):
            sut.insert_note(f"A_{i}", f"B_{i}")
        notes = sut.get_notes()
        self.assertEqual(len(notes), 6)
        for i in range(1, 6):
            self.assertEqual(notes[i].id_value, i + 1)
            self.assertEqual(notes[i].name, f"A_{i-1}")
            self.assertEqual(notes[i].description, f"B_{i-1}")

        # insert some technologies
        for i in range(0, 5):
            sut.insert_technology(f"A_{i}")
        technologies = sut.get_technologies()
        self.assertEqual(len(technologies), 6)
        for i in range(1, 6):
            self.assertEqual(technologies[i].id_value, i + 1)
            self.assertEqual(technologies[i].name, f"A_{i-1}")

        # insert some questions
        for i in range(0, 5):
            sut.insert_question(f"A_{i}", f"B_{i}")
        questions = sut.get_questions()
        self.assertEqual(len(questions), 6)
        for i in range(1, 6):
            self.assertEqual(questions[i].id_value, i + 1)
            self.assertEqual(questions[i].question, f"A_{i-1}")
            self.assertEqual(questions[i].answer, f"B_{i-1}")

        # delete one note
        note_to_delete = notes[0]
        sut.delete_note(note_to_delete)
        notes = sut.get_notes()
        self.assertEqual(len(notes), 5)
        for i in range(0, 5):
            self.assertEqual(notes[i].id_value, i + 2)
            self.assertEqual(notes[i].name, f"A_{i}")
            self.assertEqual(notes[i].description, f"B_{i}")

        # delete one technology
        technology_to_delete = technologies[0]
        sut.delete_technology(technology_to_delete)
        technologies = sut.get_technologies()
        self.assertEqual(len(technologies), 5)
        for i in range(0, 5):
            self.assertEqual(technologies[i].id_value, i + 2)
            self.assertEqual(technologies[i].name, f"A_{i}")

        # delete one question
        question_to_delete = questions[0]
        sut.delete_question(question_to_delete)
        questions = sut.get_questions()
        self.assertEqual(len(questions), 5)
        for i in range(0, 5):
            self.assertEqual(questions[i].id_value, i + 2)
            self.assertEqual(questions[i].question, f"A_{i}")
            self.assertEqual(questions[i].answer, f"B_{i}")

        # update one note
        note_to_update = notes[4]
        sut.update_note(note_to_update, "C", "D")
        self.assertEqual(note_to_update.id_value, 6)
        self.assertEqual(note_to_update.name, "C")
        self.assertEqual(note_to_update.description, "D")
        notes = sut.get_notes()
        self.assertEqual(len(notes), 5)

        # update one technology
        technology_to_update = technologies[4]
        sut.update_technology(technology_to_update, "E")
        self.assertEqual(technology_to_update.id_value, 6)
        self.assertEqual(technology_to_update.name, "E")
        technologies = sut.get_technologies()
        self.assertEqual(len(technologies), 5)

        # update one question
        question_to_update = questions[4]
        sut.update_question(question_to_update, "F", "G")
        self.assertEqual(question_to_update.id_value, 6)
        self.assertEqual(question_to_update.question, "F")
        self.assertEqual(question_to_update.answer, "G")
        questions = sut.get_questions()
        self.assertEqual(len(questions), 5)

        # drop database
        os.remove(DatabaseTest.database_name)
