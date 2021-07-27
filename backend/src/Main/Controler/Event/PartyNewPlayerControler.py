from flask import Request

from backend.src.Main.Model.Game import Game
from backend.src.Main.Model.Party import Party
from backend.src.Main.Model.Player import Player


def party_new_player_controller(request: Request, json, game: Game, socketio, message_received):
    # Je recupere le player et la game correspondant
    party: Party = game.get_party_static()
    player: Player = game.get_player_static()
    if party is not None and player is not None:
        player.last_session_id = request.sid

        # Je rajoute le player
        party.add_player(player)
        # On recupere la liste de tout les player pour les renvoyer
        to_return = {"players": party.get_pseudo_player_list()}

        party.send_event_to_player("Evt_party_new_player_as_join", to_return, socketio,
                                   message_received)
        # socketio.emit("Evt_party_new_player_as_join",jsonlib.dumps(listParty), callback=messageReceived)
