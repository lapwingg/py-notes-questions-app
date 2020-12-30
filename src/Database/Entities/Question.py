class Question:
    id = 0
    question = "Question"
    answer = "Answer"

    def __init__(self, data):
        self.id = data[0]
        self.question = data[1]
        self.answer = data[2]
