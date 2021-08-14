import random
import string

from backend.src.Main.Model.Player import Player
from backend.src.Main.Model.Question.question import Question


class Response:
    def __init__(self, response: str, player: Player, question: Question, position: int):
        self.player: Player = player
        self.question: Question = question
        self.position = position
        self.response: str = response
        self.id = self.generate_random_id(8);
        self.corect = 0;
        self.incorect = 0;

    def generate_random_id(self, size):
        return ''.join(random.choices(string.ascii_uppercase + string.digits, k=size))

    def isCorect(self):
        self.corect +=1;
    def isIncorect(self):
        self.incorect +=1;

    def is_valid_aswer(self):
        if self.incorect>self.corect or (self.incorect==0 and self.corect ==0):
            return False
        return True