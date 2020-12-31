"""note.py"""


class Note:
    """Object representing a note"""
    id_value = 0
    name = "note"
    description = "description"

    def __init__(self, data):
        self.id_value = data[0]
        self.name = data[1]
        self.description = data[2]
