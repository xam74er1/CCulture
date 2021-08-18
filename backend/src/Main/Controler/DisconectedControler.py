from flask import Request

from backend.src.Main.Model.Game import Game
from backend.src.Main.Model.Party import Party
from backend.src.Main.Model.Player import Player


def DisconectControler(request: Request, json, game: Game, socketio, message_received):
    try:
        player: Player = game.get_player_static()
    except Exception:
        return

    player.is_active = False

def ConnectControler(request: Request, json, game: Game, socketio, message_received):
    try:
        player: Player = game.get_player_static()
    except Exception:
        return

    player.is_active = True