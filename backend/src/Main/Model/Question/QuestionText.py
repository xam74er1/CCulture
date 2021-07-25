from backend.src.Main.Model.Question.question import Question


class QuestionText(Question):
    def __init__(self, question:str, response:str,categorie:str="default"):
        super().__init__(0, "text")
        self.question = question
        self.response = response
        self.categorie = categorie