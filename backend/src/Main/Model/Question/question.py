class Question:
    def __init__(self, id=0, category=""):
        self.id = id
        self.category = category
        self.time = 5  # seconde par question

    def get_json(self):
        return self.__dict__
