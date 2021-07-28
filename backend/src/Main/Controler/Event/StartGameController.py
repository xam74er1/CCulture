from flask import Request

from backend.src.Main.Model.Game import Game
from backend.src.Main.Model.Party import Party


def start_game_controller(request: Request, json, game: Game, socketio, message_received):
    print("Start game")
    party: Party = game.get_party_static()
    game.add_party_start(party)
    party.send_event_to_player("Evt_party_game_started", {"message": "Début de la partie"}, socketio, message_received)
