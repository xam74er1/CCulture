

from src.Main.Model import Game
from src.Main.Model.Party import Party
import json as jsonlib



def partyNewPlayerControler(json,game:Game,socketio,messageReceived):
    partyid = json["partyId"]
    playerId = json["playerId"]

    #Je recupre le player et la game corespondant
    party : Party = game.getParty(partyid)
    player = game.getPlayerFromUUID(playerId)


    print("Un pbr avec l'ajout du player "+playerId)
    #Je rajoute le player
    party.addPlayer(player)
    #On recupre la iste de tout les player pour les renvoyer
    listParty = party.getPseudo_Player_List();

    socketio.emit("Evt_party_new_player_as_join",jsonlib.dumps(listParty), callback=messageReceived)