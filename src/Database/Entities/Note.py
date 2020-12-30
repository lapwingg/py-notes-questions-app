class Note:
    id = 0
    name = "note"
    description = "description"

    def __init__(self, data):
        self.id = data[0]
        self.name = data[1]
        self.description = data[2]
