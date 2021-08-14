class Question:
    def __init__(self, id=0, category=""):
        self.id = id
        self.category = category
        self.time = 2  # seconde par question
        self.type = str(type(self))

    def get_json(self):
        return self.__dict__
