from typing import Dict

from flask import Request

from backend.src.Main.Model.Game import Game
from backend.src.Main.Model.Party import Party
from backend.src.Main.Model.Question.Response import Response

'''
Permet d'affiche la liste des reponce en cour
'''


def displays_current_answer(request: Request, json, game: Game, socketio, message_received):
    party: Party = game.get_party_static()
    all_player_answer = party.get_curent_question_with_all_player()

    # On ne recupere que les info uttile
    res: Dict = {}

    print(all_player_answer)
    # Si ya un bug et que aucune donne n'est retoune
    if len(all_player_answer) < 1:
        print("Un pbr est survenus : " + str(party.answer_counter))
        return
    res["question"] = all_player_answer[0].question.get_json()

    all_responses = []
    for rep in all_player_answer:
        rep: Response = rep

        element = {
            "name": rep.player.name,
            "answer": rep.response,
            "valid": (len(rep.response) > 0),
            "id": rep.id,
            "position": rep.position
        }

        all_responses.append(element)

    res["allResponse"] = all_responses

    res["isLast"]: False

    party.send_event_to_player("Evt_party_send_new_answers", res, socketio, None)
