from flask import Request

from backend.src.Main.Controler.Event.DisplayAnswerControler import displays_current_answer
from backend.src.Main.Model.Game import Game
from backend.src.Main.Model.Party import Party
from backend.src.Main.Model.Player import Player
from backend.src.Main.Model.Question.Response import Response
from backend.src.Main.Model.Question.question import Question

'''
Vue que je n'est pas d'amis je met les reponce a leur place
'''


def auto_fill_party_wth_answer(request: Request, json, game: Game, socketio, message_received):
    party: Party = game.get_party_static()
    player: Player = game.get_player_static()

    playerA: Player = Player("Palyer B")
    playerB: Player = Player("Palyer C")

    party.add_player(playerA)
    party.add_player(playerB)

    i = 0;
    for question in party.questionList:
        question: Question = question
        c = 'A'
        for playerL in party.playerList:
            playerL: Player = playerL
            #print(playerL.name)
            rep = Response("Reponce for player " + playerL.name + " for question " + str(i), playerL, question, i)
            party.add_reponce(rep)

        i += 1
    displays_current_answer(request, json, game, socketio, message_received)
