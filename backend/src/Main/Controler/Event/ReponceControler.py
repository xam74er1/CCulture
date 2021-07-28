from flask import Request

from backend.src.Main.Model.Game import Game
from backend.src.Main.Model.Party import Party
from backend.src.Main.Model.Player import Player
from backend.src.Main.Model.Question.question import Question


def reponce_controler(request: Request, js, game: Game, socketio, message_received):
    party: Party = game.get_party_static()
    player : Player = game.get_player_static()
    question : Question = party.get_current_question()