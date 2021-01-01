"""info_view_model.py"""
from src.database.database import Database


class InfoViewModel:
    """View model supports Info view"""
    developer = 'lapwingg'
    app_version = '0.1'
    commit_hash = '4601b64d'
    py_qt_version = '5.15.2'
    python_version = '3.9'

    @classmethod
    def notes_count(cls):
        """Returns notes count in the database"""
        return len(Database().get_notes())

    @classmethod
    def technologies_count(cls):
        """Returns technologies count in the database"""
        return len(Database().get_technologies())

    @classmethod
    def questions_count(cls):
        """Returns questions count in the database"""
        return len(Database().get_questions())
