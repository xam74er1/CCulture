from backend.src.Main.Model.Question.question import Question


class QuestionText(Question):
    def __init__(self, question: str, response: str,id=0, category: str = "default"):
        super().__init__(id, category)
        self.question = question
        self.response = response
        self.type = str(type (self));
