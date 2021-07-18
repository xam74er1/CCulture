from flask import Request, redirect, session, flash
import json as js



from src.Main.Model.Game import Game
from src.Main.Model.Party import Party
from src.Main.Model.Player import Player

#Todo : Pense a rajoute la liste des player dans le controler
#Todo : Pense dans le cas ou les champ game_id , sid ou pseude est null
#Todo : refaire le systeme avec le form lors du join
def JoinControler(request : Request ,json,game:Game,socketio,messageReceived):
   # print("Join")

   # form = request.form
    if "gameId" in json :
        game_id = json["gameId"]
    else:
        game_id = None
    sid = request.sid
    pseudo = json["pseudoId"]

    #Creation du player si il nexiste pas
    if 'uuid' in session:
        # Le player existe deja
        uuid = session["uuid"]
        player : Player =  game.getPlayerFromUUID(uuid)
        #Il ce peux que le uuid existe dans le session mais pas dans la game dans ce cas nous cree un nvx player
        if not player:
            player = Player(pseudo, sid)
            session["uuid"] = player.uuid;
            game.addPlayer(player)

    else:
        print("PLayer not exist we ceate him")
        #Le player n'existe pas donc on le cree
        player = Player(pseudo,sid)
        session["uuid"] = player.uuid;
        game.addPlayer(player)
        #session["object"] = player


    session["pseudo"] = player.name





    if not game_id or game_id==None:

        party = Party();
        game.addParty(party)
    else :
        party = game.getParty(game_id)

    if party != None:

        url = "/party/"+str(party.id);
        player.curent_party_id= party.id

        Game.getGame()

        toReturn = {}
        toReturn["url"] = url;
        toReturn["playerID"] = player.uuid
        socketio.emit("Evt_redirect_gameid", js.dumps(toReturn), room=sid, callback=messageReceived)

        return url
        #return redirect(url);
    print("Redirect to join")

    return redirect('/join');


def ack():
    print("msg receilve")