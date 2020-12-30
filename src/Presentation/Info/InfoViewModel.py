from src.Database.Database import Database


class InfoViewModel:
    developer = 'lapwingg'
    app_version = '0.1'
    commit_hash = 'c4b33f9'
    py_qt_version = '5.15.2'
    python_version = '3.9'

    @classmethod
    def notes_count(cls):
        return len(Database().get_notes())

    @classmethod
    def technologies_count(cls):
        return len(Database().get_technologies())

    @classmethod
    def questions_count(cls):
        return len(Database().get_questions())
