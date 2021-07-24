from flask import Request

from backend.src.Main.Model.Game import Game
from backend.src.Main.Model.Party import Party
from backend.src.Main.Model.Player import Player
from backend.src.Main.Model.Question.question import Question


def get_question(request: Request, js, game: Game, socketio, message_received):
    party: Party = game.get_party_static()
    player: Player = game.get_player_static()
    # Par sécurite on lui remet son SID
    player.last_session_id = request.sid
    question: Question = party.get_curent_question()
    # On ne renvois la question que a celui qui la demande
    socketio.emit('my question', question.get_json(),
                  callback=message_received, room=player.last_session_id)
