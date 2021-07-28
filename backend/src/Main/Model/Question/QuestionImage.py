import QuestionText


class QuestionImage(QuestionText):
    def __init__(self, image):
        self.image = image
        self.type = type(self);
