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

    party: Party = game.get_party_static()

    #Si le leader a quitter la partie
    if party.party_leader.name == player.name:
        #Si il reste au moin un joeure active on lui donne le leade
        for p in party.playerList:
            if p.is_active :
                party.party_leader = p
                break

    list_avaible_player = []
    for p in party.playerList:
        if p.is_active:
            list_avaible_player.append(p.name)

    #On notifie tout les joeure que un joeure a deco
    party.send_event_to_player("Evt_party_player_disconected",{"leader":party.party_leader.name,"player_list":list_avaible_player},socketio,None)


def ConnectControler(request: Request, json, game: Game, socketio, message_received):
    try:
        player: Player = game.get_player_static()
    except Exception:
        return

    player.is_active = True