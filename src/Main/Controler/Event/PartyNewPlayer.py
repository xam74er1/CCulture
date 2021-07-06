from flask import Request

from src.Main.Model import Game
from src.Main.Model.Party import Party
import json as jsonlib

from src.Main.Model.Player import Player


def partyNewPlayerControler(request : Request ,json,game:Game,socketio,messageReceived):
    partyid = json["partyId"]
    playerId = json["playerId"]

    #Je recupre le player et la game corespondant
    party : Party = game.getParty(partyid)
    player : Player = game.getPlayerFromUUID(playerId)

    player.last_session_id = request.sid

    print("Un pbr avec l'ajout du player "+playerId)
    #Je rajoute le player
    party.addPlayer(player)
    #On recupre la iste de tout les player pour les renvoyer
    listParty = party.getPseudo_Player_List();

    party.sendEventToPlayer("Evt_party_new_player_as_join",jsonlib.dumps(listParty),socketio,messageReceived)
    #socketio.emit("Evt_party_new_player_as_join",jsonlib.dumps(listParty), callback=messageReceived)