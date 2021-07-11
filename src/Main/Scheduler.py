from src.Main.Model import Game, Party
from src.Main.Model.Question.question import Question


def nextQuestionParty(game:Game,socketio):
    for p in game.listRuningParty:
        party : Party = p;

        #Si il reste au moin une question a affiche
        if party.compteur > 1:

            questionCurent: Question = party.questionList[party.compteur - 1]

            if party.timeLeft > questionCurent.time:
                sendNextQuestion(socketio,party)
                #On resete le conteure
                party.timeLeft = 0;

                #Si il reste aucune question a affiche



            else:
                #On incremente le conteure
                party.timeLeft = party.timeLeft+1;
        #Si on est a la dernire question
        else :
            questionCurent: Question = party.questionList[0]
            #Si la question actulle a depasse le temps reglmentaire on termine la partie
            if party.timeLeft > questionCurent.time:
                termiatedParty(game,party,socketio)
            else:
                #Si non on continue d'incremente le timer
                party.timeLeft = party.timeLeft + 1;


def sendNextQuestion(socketio,party:Party):
    party.compteurDown()
    questionCurent: Question = party.getCurentQuestion()
    print("Send question" + questionCurent.get_json())

    party.sendEventToPlayer("my question", questionCurent.get_json(), socketio, None)

def termiatedParty(game:Game,party:Party,socketio):
    print("Party terminated")
    game.removeParty(party)
    party.sendEventToPlayer("partyTerminated", "", socketio, None)