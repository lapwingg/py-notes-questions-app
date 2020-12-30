from os.path import exists
import sqlite3

from src.Database.Entities.Note import Note
from src.Database.Entities.Technology import Technology
from src.Database.Entities.Question import Question


class Database:
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
        data = self.__execute_query_for_data("""
            SELECT * from note
        """)
        return [Note(d) for d in data]

    def get_technologies(self):
        data = self.__execute_query_for_data("""
            SELECT * from technology
        """)
        return [Technology(d) for d in data]

    def get_questions(self):
        data = self.__execute_query_for_data("""
            SELECT * from question
        """)
        return [Question(d) for d in data]

    # Insert

    def insert_note(self, name, description):
        self.__execute_query(f"""
            INSERT INTO note(name, description) VALUES ('{name}', '{description}')
        """)

    def insert_technology(self, name):
        self.__execute_query(f"""
            INSERT INTO technology(name) VALUES ('{name}')
        """)

    def insert_question(self, question, answer):
        self.__execute_query(f"""
            INSERT INTO question(question, answer) VALUES ('{question}', '{answer}')
        """)

    def delete_note(self, note):
        self.__execute_query(f"""
            DELETE FROM note WHERE id = {note.id}
        """)

    def delete_technology(self, technology):
        self.__execute_query(f"""
            DELETE FROM technology WHERE id = {technology.id}
        """)

    def delete_question(self, question):
        self.__execute_query(f"""
            DELETE FROM question WHERE id = {question.id}
        """)

    def update_note(self, note, new_name=None, new_description=None):
        queries = []
        if new_name:
            queries.append(f"""
                    UPDATE note SET name = '{new_name}' WHERE id = {note.id}
                """)
            note.name = new_name

        if new_description:
            queries.append(f"""
                    UPDATE note SET description = '{new_description}' WHERE id = {note.id}
                """)
            note.description = new_description

        if queries:
            self.__execute_queries(queries)

    def update_technology(self, technology, new_name=None):
        if new_name:
            self.__execute_query(f"""
                UPDATE technology SET name = '{new_name}' WHERE id = {technology.id}
            """)
            technology.name = new_name

    def update_question(self, question, new_question=None, new_answer=None):
        queries = []
        if new_question:
            queries.append(f"""
                UPDATE question SET question = '{new_question}' WHERE id = {question.id}
            """)
            question.question = new_question

        if new_answer:
            queries.append(f"""
                UPDATE question SET answer = '{new_answer}' WHERE id = {question.id}
            """)
            question.answer = new_answer

        if queries:
            self.__execute_queries(queries)
