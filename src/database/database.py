"""database.py"""
from os.path import exists
import sqlite3

from src.database.entities.note import Note
from src.database.entities.technology import Technology
from src.database.entities.question import Question


class Database:
    """Class used to contact with database"""
    database_name = "project.db"

    def __init__(self, database_name="project.db"):
        self.database_name = database_name

        if not exists(self.database_name):
            self.__create_database()

    def __execute_query(self, query):
        self.__execute_queries([query])

    def __execute_queries(self, queries):
        connection = sqlite3.connect(self.database_name)
        cursor = connection.cursor()
        for query in queries:
            cursor.execute(query)
        connection.commit()

    def __execute_query_for_data(self, query):
        connection = sqlite3.connect(self.database_name)
        cursor = connection.cursor()
        cursor.execute(query)
        return cursor.fetchall()

    def __create_database(self):
        queries = ["""
                CREATE TABLE note
                (id INTEGER PRIMARY KEY, name TEXT, description TEXT)
            """,
            """
                CREATE TABLE technology
                (id INTEGER PRIMARY KEY, name TEXT)
            """,
            """
                CREATE TABLE question
                (id INTEGER PRIMARY KEY, question TEXT, answer TEXT)
            """]
        self.__execute_queries(queries)

    def get_notes(self):
        """Returns all stored notes"""
        data = self.__execute_query_for_data("""
            SELECT * from note
        """)
        return [Note(d) for d in data]

    def get_technologies(self):
        """Returns all stored technologies"""
        data = self.__execute_query_for_data("""
            SELECT * from technology
        """)
        return [Technology(d) for d in data]

    def get_questions(self):
        """Returns all stored questions"""
        data = self.__execute_query_for_data("""
            SELECT * from question
        """)
        return [Question(d) for d in data]

    # Insert

    def insert_note(self, name, description):
        """Inserts a note into database"""
        self.__execute_query(f"""
            INSERT INTO note(name, description) VALUES ('{name}', '{description}')
        """)

    def insert_technology(self, name):
        """Inserts a technology into database"""
        self.__execute_query(f"""
            INSERT INTO technology(name) VALUES ('{name}')
        """)

    def insert_question(self, question, answer):
        """Inserts a question into database"""
        self.__execute_query(f"""
            INSERT INTO question(question, answer) VALUES ('{question}', '{answer}')
        """)

    def delete_note(self, note):
        """Deletes given note from database"""
        self.__execute_query(f"""
            DELETE FROM note WHERE id = {note.id_value}
        """)

    def delete_technology(self, technology):
        """Deletes given technology from database"""
        self.__execute_query(f"""
            DELETE FROM technology WHERE id = {technology.id_value}
        """)

    def delete_question(self, question):
        """Deletes given question from database"""
        self.__execute_query(f"""
            DELETE FROM question WHERE id = {question.id_value}
        """)

    def update_note(self, note, new_name=None, new_description=None):
        """Update given note in database and its object"""
        queries = []
        if new_name:
            queries.append(f"""
                    UPDATE note SET name = '{new_name}' WHERE id = {note.id_value}
                """)
            note.name = new_name

        if new_description:
            queries.append(f"""
                    UPDATE note SET description = '{new_description}' WHERE id = {note.id_value}
                """)
            note.description = new_description

        if queries:
            self.__execute_queries(queries)

    def update_technology(self, technology, new_name=None):
        """Update given technology and its object"""
        if new_name:
            self.__execute_query(f"""
                UPDATE technology SET name = '{new_name}' WHERE id = {technology.id_value}
            """)
            technology.name = new_name

    def update_question(self, question, new_question=None, new_answer=None):
        """Update given question and its object"""
        queries = []
        if new_question:
            queries.append(f"""
                UPDATE question SET question = '{new_question}' WHERE id = {question.id_value}
            """)
            question.question = new_question

        if new_answer:
            queries.append(f"""
                UPDATE question SET answer = '{new_answer}' WHERE id = {question.id_value}
            """)
            question.answer = new_answer

        if queries:
            self.__execute_queries(queries)
