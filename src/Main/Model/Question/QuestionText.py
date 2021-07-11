from . import question
from .question import Question


class QuestionText(Question):
    def __init__(self, question, reponse):
        super().__init__(0,"text")
        self.question = question;
        self.reponse = reponse
