import random  # define the random module
import string

from backend.src.Main.Model.Player import Player
from backend.src.Main.Model.Question import question
from backend.src.Main.Model.Question.QuestionImage import QuestionImage
from backend.src.Main.Model.Question.QuestionText import QuestionText
from backend.src.Main.Model.Question.Response import Response


class Party:
    def __init__(self, counter=0, question_list=[]):
        self.id: str = self.generate_random_url(10)
        self.playerList: [Player] = []
        self.questionList: [question] = question_list
        self.counter: int = counter
        self.timeLeft = 0
        self.generate_question()
        self.listReponce: [Response] = [];

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

    def get_player_list(self):
        plist = []

        for player in self.playerList:
            plist.append({"id": player.uuid, "name": player.name})
        return plist

    def send_event_to_player(self, event_name, json, socketio, message_received):
        for p in self.playerList:
            if message_received is None:
                socketio.emit(event_name, json, room=p.last_session_id, callback=self.ack())
            else:
                socketio.emit(event_name, json, callback=message_received, room=p.last_session_id)

    def ack(self):
        print("msg receive")

    def counter_up(self):
        self.counter = self.counter + 1

    def counter_down(self):
        self.counter = self.counter - 1

    def get_current_question(self):
        if len(self.questionList) > 0 and -1 < self.counter <= len(self.questionList):
            return self.questionList[self.counter - 1]
        else:
            return None

    def generate_question(self):
        self.questionList = [QuestionText('Qui Mange des Pomme', 'Chirac'),
                             QuestionText('Qui Mange des Pomme2', 'Chirac'),
                             QuestionText('Qui Mange des Pomme3', 'Chirac'),
                             QuestionImage("comment s'appele ce chat ?",response="chat kira",imagePath="backend/ressouces/images/Test/chatKira.jpg",isBase64=True,category="Test")
                             ]
        self.counter = len(self.questionList)

    def add_reponce(self, reponce: Response):
        self.listReponce.append(reponce)

    '''
    postion = postion de la question voulus
    player_position = pour un player donne sa position
    
    :param postion a -1 pour recupere toute les reponce
    :param pplayer_postion a -1 pour n'importe quelle player
       '''

    def get_all_reponece(self, position=-1, player_position=-1):
        # SI on ne lui met pas d'argument cest que lon veux toute les reponce
        if (position == -1):
            return self.listReponce

        # Si on afiche les player un par un
        if player_position != -1:
            curent_player: Player = self.playerList[player_position]

        # Si non on affiche que ceux corepondant a la question
        toReturn = []
        for rep in self.listReponce:
            rep: Response = rep
            if rep.position == position:
                # Si nous chersson un player en particulier et que ce player corepond
                if player_position != -1 and rep.player.name == curent_player.name:
                    toReturn.append(rep)
                else:
                    toReturn.append(rep)
        return rep
