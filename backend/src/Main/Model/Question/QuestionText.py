from backend.src.Main.Model.Question.question import Question


class QuestionText(Question):
    def __init__(self, question, response):
        super().__init__(0, "text")
        self.question = question
        self.response = response
