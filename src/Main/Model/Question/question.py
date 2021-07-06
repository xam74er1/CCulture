import json
class question():
    def __init__(self, id, categorie):
        self.id=id;
        self.categorie=categorie;
        
    def get_json(self):
        return json.dumps(self.__dict__)