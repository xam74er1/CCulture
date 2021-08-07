from flask import Request

from backend.src.Main.Controler.Event.DisplayAnswerControler import displays_curent_answer
from backend.src.Main.Model.Game import Game
from backend.src.Main.Model.Party import Party
from backend.src.Main.Model.Question.question import Question

'''
Controleur permtant d'affecte lrosque les joeure dise si une reponce est valide ou non
'''
def set_valid_answer(request: Request, json, game: Game, socketio, message_received):
    party: Party = game.get_party_static()
    print(json)
    #Pour tous les player on set la reponce si elle est valide ou non
    for rep in json:
        party.set_valid_aswer(rep)

    party.increase_validation_count();

    #Si tout les player on envoyer leur reponce
    if party.nb_player_send_validation >= len(party.playerList):
        #On decremente le conteure
        party.nb_player_send_validation = 0;
        party.next_aswer()
        #Si il reste au moin une question a afficher
        if party.answer_counter>0 :
            #On envois la question suivante
            displays_curent_answer(request, json, game, socketio, message_received)
        else:
            #Si non on affiche les resulta
            print("Displays result")