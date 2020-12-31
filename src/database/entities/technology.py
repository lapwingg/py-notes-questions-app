"""technology.py"""


class Technology:
    """Object representing a technology"""
    id_value = 0
    name = "Name"

    def __init__(self, data):
        self.id_value = data[0]
        self.name = data[1]
