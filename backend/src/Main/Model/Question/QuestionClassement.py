import question


class QuestionClassement(question):
    def __init__(self, classable, question):
        self.classable = classable
        self.question = question
        self.type = str(type (self));
