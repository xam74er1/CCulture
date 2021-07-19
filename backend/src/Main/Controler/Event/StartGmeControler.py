from flask import Request, render_template

from backend.src.Main.Model.Game import Game
from backend.src.Main.Model.Party import Party


def start_game_controller(request: Request, json, game: Game, socketio, message_received):
    print("Start game")
    party: Party = game.get_party_static()
    game.add_party_start(party)
    json_to_return = render_template('testQuestion.html')
    party.send_event_to_player("partyStart", json_to_return, socketio, message_received)
