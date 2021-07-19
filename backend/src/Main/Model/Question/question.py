import json


class Question:
    def __init__(self, id=0, categorie=""):
        self.id = id
        self.categorie = categorie
        self.time = 5  # seconde par question

    def get_json(self):
        return json.dumps(self.__dict__)
