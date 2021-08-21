import random

from backend.src.Main.Model.Question.QuestionTree.QuestionTree import QuestionTree
from backend.src.Main.Model.Question.question import Question


class QuestionLeaves(QuestionTree):
    def __init__(self, question_list: [Question], name: str = "root", poids=1):
        super().__init__(name, poids)
        self.question_list : [Question] = question_list

    def get_question(self):
        self.getRandomQuestion(self.question_list)

    def getRandomQuestion(question_list: [Question]):
        return random.choice(question_list)
        