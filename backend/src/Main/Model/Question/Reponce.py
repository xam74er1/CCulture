from backend.src.Main.Model.Player import Player
from backend.src.Main.Model.Question.question import Question


class Reponce:
    def __init__(self,reponce:str,player:Player,question:Question,position:int):
        self.player : Player = player
        self.question : Question = question
        self.position = position
        self.reponce : str = reponce