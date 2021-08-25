from flask import Request

from backend.src.Main.Model.Game import Game
from backend.src.Main.Model.Party import Party
from backend.src.Main.Model.Player import Player


def party_new_player_controller(request: Request, json, game: Game, socketio, message_received):
    # Je recupere le player et la game correspondant
    try:
        party: Party = game.get_party_static()
        player: Player = game.get_player_static()
    except Exception:
        party = None
        player = None

    if party is not None and player is not None:
        if json == party.id:
            player.last_session_id = request.sid

            # Si le pseudo existe deja nous ne l'autorison pas a rejoindre
            if party.havePlayerName(player.name):

                find = False
                # On chersse si le player le player avec le meme nom est deco , si cela est le cas on lui permet de ce reconected
                for p in party.playerList:
                    if p.name == player.name and not p.is_active:
                        # On a trouve le player in le fait donc ce reconnecte
                        find = True
                        p: Player = p
                        p.last_session_id = player.last_session_id
                        p.uuid = player.uuid
                        p.is_active = True
                        player = p
                        connect_player(party, socketio, message_received)
                        return

                if not find:
                    socketio.emit("Evt_error",
                                  "Impossile de rejoindre la party : Il y a deja un joeur avec le pseudo " + player.name,
                                  room=request.sid,
                                  callback=message_received)
                    return

            # Je rajoute le player
            party.add_player(player)
            # On recupere la liste de tout les player pour les renvoyer
            connect_player(party,player, socketio, message_received)
        else:
            socketio.emit("Evt_error",
                          "Vous ne pouvez pas rejoindre cette partie ! (Vous avez rejoin la mauvaise partie , merci de passer par join)",
                          room=request.sid, callback=message_received)
        # socketio.emit("Evt_party_new_player_as_join",jsonlib.dumps(listParty), callback=messageReceived)
    else:
        socketio.emit("Evt_error", "Vous ne pouvez pas rejoindre cette partie ! (passer dabore par join)",
                      room=request.sid, callback=message_received)


def connect_player(party: Party,player, socketio, message_received):
    # On recupere la liste de tout les player pour les renvoyer
    to_return = {"players": party.get_player_list(),"player_name":player.name,"leader": party.party_leader.name}

    party.send_event_to_player("Evt_party_new_player_as_join", to_return, socketio,
                               message_received)
