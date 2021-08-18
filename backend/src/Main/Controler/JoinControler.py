from flask import Request, session

# Todo : Pense a rajoute la liste des player dans le controler
# Todo : Pense dans le cas ou les champ game_id , sid ou pseude est null
# Todo : refaire le systeme avec le form lors du join
from backend.src.Main.Model.Game import Game
from backend.src.Main.Model.Party import Party
from backend.src.Main.Model.Player import Player


def join_controller(request: Request, json, game: Game, socketio, message_received):
    print("Evt_join_game")

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
            session["uuid"] = player.uuid
            game.add_player(player)

    else:
        print("PLayer not exist we ceate him")
        # Le player n'existe pas donc on le cree
        player = Player(pseudo, sid)
        session["uuid"] = player.uuid
        game.add_player(player)
        # session["object"] = player

    session["pseudo"] = player.name

    if not game_id or game_id is None:

        party = Party()
        game.add_party(party)
    else:
        party = game.get_party(game_id)

    if party is not None:
        player.current_party_id = party.id

        #Si le pseudo existe deja nous ne l'autorison pas a rejoindre
        if party.havePlayerName(player.name):
            socketio.emit("Evt_error", "Il y a deja un joeur avec le pseudo "+player.name, room=sid, callback=message_received)
            return
        Game.get_game()

        to_return = {"party_id": party.id, "player_id": player.uuid}
        socketio.emit("Evt_redirect_game_id", to_return, room=sid, callback=message_received)

        return
    print("Cette partie n'existe pas")
    # SI on arrive ici cest que la partie n'existe pas
    socketio.emit("Evt_error", "Cette partie n'existe pas", room=sid, callback=message_received)


def ack():
    print("msg receive")
