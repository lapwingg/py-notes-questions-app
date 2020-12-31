"""question.py"""


class Question:
    """Object representing a question"""
    id_value = 0
    question = "Question"
    answer = "Answer"

    def __init__(self, data):
        self.id_value = data[0]
        self.question = data[1]
        self.answer = data[2]
