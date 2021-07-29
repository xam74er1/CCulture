from backend.src.Main.Model.Player import Player
from backend.src.Main.Model.Question.question import Question


class Response:
    def __init__(self, response: str, player: Player, question: Question, position: int):
        self.player: Player = player
        self.question: Question = question
        self.position = position
        self.response: str = response
