import random  # define the random module
import string

from backend.src.Main.Model.Player import Player
from backend.src.Main.Model.Question import question
from backend.src.Main.Model.Question.QuestionText import QuestionText


class Party():
    def __init__(self, compteur=0, question_list=[]):
        self.id: str = self.generate_random_url(10)
        self.playerList: [Player] = []
        self.questionList: [question] = question_list
        self.compteur: int = compteur
        self.timeLeft = 0;
        self.generate_question()

    def generate_random_url(self, size):
        return ''.join(random.choices(string.ascii_uppercase + string.digits, k=size))

    def add_player(self, player):
        self.playerList.append(player)

    def get_pseudo_player_list(self):
        plist = []

        for p in self.playerList:
            print(p)
            plist.append(p.name)
        return plist

    def send_event_to_player(self, event_name, json, socketio, message_received):
        for p in self.playerList:
            if message_received is None:
                socketio.emit(event_name, json, room=p.last_session_id, callback=self.ack())
            else:
                socketio.emit(event_name, json, callback=message_received, room=p.last_session_id)

    def ack(self):
        print("msg receilve")

    def compteur_up(self):
        self.compteur = self.compteur + 1

    def compteur_down(self):
        self.compteur = self.compteur - 1

    def get_curent_question(self):
        if len(self.questionList) > 0 and -1 < self.compteur <= len(self.questionList):
            return self.questionList[self.compteur - 1]
        else:
            return None;

    def generate_question(self):
        self.questionList = [QuestionText('Qui Mange des Pomme', 'Chirac'),
                             QuestionText('Qui Mange des Pomme2', 'Chirac'),
                             QuestionText('Qui Mange des Pomme3', 'Chirac')];
        self.compteur = len(self.questionList)
