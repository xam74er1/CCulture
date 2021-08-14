from flask import Request

from backend.src.Main.Controler.Event.DisplayAnswerControler import displays_current_answer
from backend.src.Main.Model.Game import Game
from backend.src.Main.Model.Party import Party
from backend.src.Main.Model.Question import Response

'''
Controleur permtant d'affecte lrosque les joeure dise si une reponce est valide ou non
'''


def set_valid_answer(request: Request, json, game: Game, socketio, message_received):
    party: Party = game.get_party_static()
    print(json)
    # Pour tous les player on set la reponce si elle est valide ou non
    for rep in json:
        party.set_valid_aswer(rep)

    party.increase_validation_count()

    # Si tout les player on envoyer leur reponce
    if party.nb_player_send_validation >= len(party.playerList):
        # On decremente le conteure
        party.nb_player_send_validation = 0
        party.next_aswer()
        # Si il reste au moin une question a afficher
        if party.answer_counter > 0:
            # On envois la question suivante
            displays_current_answer(request, json, game, socketio, message_received)
        else:
            # Si non on affiche les resulta
            print("Displays result")
            for aw in party.listReponce:
                rep: Response = aw
                print(str(rep.response) + " :  +" + str(rep.corect) + " " + str(rep.incorect))

            res = get_player_score(party);
            print(res)
            party.send_event_to_player("Evt_party_final_results", res, socketio, None)


def get_player_score(party : Party):
    result = []
    for player  in party.playerList:
        print("Pour le joeure"+player.name)
        all_reponce = party.get_all_reponce_for_player(player)
        conteur = 0
        for rep  in all_reponce:
            if rep.is_valid_aswer():
               conteur += 1
               print("Nombre de point : "+str(conteur)+"  "+str(rep.is_valid_aswer()))
        result.append({
            "name" : player.name,
            "points" : conteur
        })

    print("Avant "+str(result))
    result = sorted(result, key=lambda k: k['points'],reverse=True)
    postion = 1;
    for tmp in result:
        tmp["rank"] = postion
        postion+=1
    return {"result":result}