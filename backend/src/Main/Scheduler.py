from backend.src.Main.Model.Game import Game
from backend.src.Main.Model.Party import Party
from backend.src.Main.Model.Question.question import Question


def next_question_party(game: Game, socketio):
    for p in game.listRunningParty:
        party: Party = p

        # Si il reste au moins une question a affiche
        if party.counter > 1:

            question_current: Question = party.questionList[party.counter - 1]

            if party.timeLeft > question_current.time:
                send_next_question(socketio, party)
                # On reset le compteur
                party.timeLeft = 0;

                # Si il reste aucune question a afficher



            else:
                # On incremente le conteure
                party.timeLeft = party.timeLeft + 1;
        # Si on est a la dernire question
        else:
            question_current: Question = party.questionList[0]
            # Si la question actulle a depasse le temps reglmentaire on termine la partie
            if party.timeLeft > question_current.time:
                termiated_party(game, party, socketio)
            else:
                # Si non on continue d'incremente le timer
                party.timeLeft = party.timeLeft + 1;


def send_next_question(socketio, party: Party):
    party.counter_down()
    question_curent: Question = party.get_current_question()
    print("Send question" + question_curent.get_json())

    party.send_event_to_player("my question", question_curent.get_json(), socketio, None)


def termiated_party(game: Game, party: Party, socketio):
    print("Party terminated")
    game.remove_party(party)
    party.send_event_to_player("partyTerminated", "", socketio, None)
