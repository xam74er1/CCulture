from flask import Request

import json as jsonlib

from backend.src.Main.Model.Game import Game
from backend.src.Main.Model.Party import Party
from backend.src.Main.Model.Player import Player


def party_new_player_controller(request: Request, json, game: Game, socketio, message_received):
    # Je recupere le player et la game correspondant
    try :
        party: Party = game.get_party_static()
        player: Player = game.get_player_static()
    except Exception:
        party = None;
        player = None;

    if party is not None and player is not None:
        if json == party.id :
            player.last_session_id = request.sid

            # Je rajoute le player
            party.add_player(player)
            # On recupere la liste de tout les player pour les renvoyer
            to_return = {"players": party.get_player_list()}

            party.send_event_to_player("Evt_party_new_player_as_join", to_return, socketio,
                                       message_received)
        else :
            socketio.emit("Evt_error", "Vous ne pouvez pas rejoindre cette partie ! (Vous avez rejoin la mauvaise partie , merci de passer par join)",
                          room=request.sid, callback=message_received)
        # socketio.emit("Evt_party_new_player_as_join",jsonlib.dumps(listParty), callback=messageReceived)
    else :
        socketio.emit("Evt_error", "Vous ne pouvez pas rejoindre cette partie ! (passer dabore par join)", room=request.sid, callback=message_received)
