import random  # define the random module
import string
import traceback

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
        self.answer_counter : int =0;
        self.timeLeft = 0
        self.generate_question()
        self.listReponce: [Response] = [];
        self.nb_player_send_validation = 0;

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

    #Retourne la question actuelle
    def get_current_question(self):
        print("Get curent question for the postion : "+str(self.counter))
        if len(self.questionList) > 0 and -1 < self.counter <= len(self.questionList):
            return self.questionList[self.counter - 1]
        else:
            return None

    #Retourne la question precedente
    def get_previous_question(self):
        return self.questionList[self.counter%len(self.questionList)]

    def generate_question(self):
        self.questionList = [QuestionText('Qui Mange des Pomme', 'Chirac'),
                             QuestionText('Qui Mange des Pomme2', 'Chirac'),
                             QuestionText('Qui Mange des Pomme3', 'Chirac'),
                             QuestionImage("comment s'appele ce chat ?",response="chat kira",imagePath="backend/ressouces/images/Test/chatKira.jpg",isBase64=True,category="Test")
                             ]
        self.counter = len(self.questionList)
        self.answer_counter =len(self.questionList)

    def add_reponce(self, reponce: Response):
        self.listReponce.append(reponce)

    '''
    postion = postion de la question voulus
    player_position = pour un player donne sa position
    
    :param postion a -1 pour recupere toute les reponce
    :param pplayer_postion a -1 pour n'importe quelle player
       '''

    def get_all_reponece(self, position=-1, player_position=-1):
        print("Conteure :"+str(position))
        #On inversse la postion pour resortir en premier les question qui on ete posse au debut
        inversed_position = len(self.listReponce)-position-1;
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
        return toReturn

    '''
    Retourne tout les uttilise pour une question donne
    '''
    def get_curent_question_with_all_player(self):
        if self.answer_counter > 0 :
            return self.get_all_reponece(self.answer_counter-1)

        print("Un bug est survenus avec un cnteure negative")
        traceback.print_stack()
        return [];


    '''
    Met a jour la reponce pour dire si elle est corecte ou non 
    
    L'auto evalation est autorise
    '''
    def set_valid_aswer(self,json):

        id = json["id"];
        valid = json["valid"]
        for rep in self.listReponce:
            if str(rep.id) == str(id) :
                if valid :
                    rep.isCorect()
                else:
                    rep.isIncorect()
                break;


    def increase_validation_count(self):
        self.nb_player_send_validation +=1;

    def next_aswer(self):
        self.answer_counter -=1;

