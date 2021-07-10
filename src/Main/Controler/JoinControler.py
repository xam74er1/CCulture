from flask import Request, redirect, session

from src.Main.Model.Game import Game
from src.Main.Model.Party import Party
from src.Main.Model.Player import Player

#Todo : Pense a rajoute la liste des player dans le controler
#Todo : Pense dans le cas ou les champ game_id , sid ou pseude est null
def JoinControler(request: Request,game : Game):
    print("Join")
    form = request.form
    game_id = form["gameId"]
    sid = form["sid"]
    pseudo = form["pseudoId"]

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


    if not game_id:
        party = Party();
        game.addParty(party)
    else :
        party = game.getParty(game_id)
    print("Party"+str(party))
    if party != None:

        url = "/party/"+str(party.id);
        player.last_session_id = party.id

        Game.getGame()

        return redirect(url);
    print("Redirect to join")

    return redirect('/join');