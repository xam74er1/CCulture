import json as js

from flask import Request, redirect, session

# Todo : Pense a rajoute la liste des player dans le controler
# Todo : Pense dans le cas ou les champ game_id , sid ou pseude est null
# Todo : refaire le systeme avec le form lors du join
from backend.src.Main.Model.Game import Game
from backend.src.Main.Model.Party import Party
from backend.src.Main.Model.Player import Player


def join_controller(request: Request, json, game: Game, socketio, message_received):
    # print("Join")

    # form = request.form
    if "gameId" in json:
        game_id = json["gameId"]
    else:
        game_id = None
    sid = request.sid
    pseudo = json["pseudoId"]

    # Creation du player si il nexiste pas
    if 'uuid' in session:
        # Le player existe deja
        uuid = session["uuid"]
        player: Player = game.get_player_from_uuid(uuid)
        # Il ce peux que le uuid existe dans le session mais pas dans la game dans ce cas nous cree un nvx player
        if not player:
            player = Player(pseudo, sid)
            session["uuid"] = player.uuid;
            game.add_player(player)

    else:
        print("PLayer not exist we ceate him")
        # Le player n'existe pas donc on le cree
        player = Player(pseudo, sid)
        session["uuid"] = player.uuid;
        game.add_player(player)
        # session["object"] = player

    session["pseudo"] = player.name

    if not game_id or game_id is None:

        party = Party()
        game.add_party(party)
    else:
        party = game.get_party(game_id)

    if party is not None:
        url = "/party/" + str(party.id)
        player.current_party_id = party.id

        Game.get_game()

        to_return = {"url": url, "playerID": player.uuid}
        socketio.emit("Evt_redirect_gameid", to_return, room=sid, callback=message_received)

        return url
        # return redirect(url);
    print("Redirect to join")

    return redirect('/join')


def ack():
    print("msg receive")
