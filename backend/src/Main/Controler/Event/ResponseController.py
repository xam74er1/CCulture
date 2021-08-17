from flask import Request

from backend.src.Main.Model.Game import Game
from backend.src.Main.Model.Party import Party
from backend.src.Main.Model.Player import Player
from backend.src.Main.Model.Question.Response import Response
from backend.src.Main.Model.Question.question import Question


def response_controller(request: Request, json, game: Game, socketio, message_received):
    if json is not None:
        party: Party = game.get_party_static()
        player: Player = game.get_player_static()
        question: Question = party.get_previous_question()
        print("Reponce recus : " + str(json) + " mise a la postion " + str(party.counter) + " for the question " + str(
            question.get_json()))
        response = Response(json, player, question, party.counter)
        party.add_reponce(response)
