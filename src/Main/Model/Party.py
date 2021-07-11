from src.Main.Model.Player import Player
from src.Main.Model.Question import question
import string
import random # define the random module
import json as jsonlib

from src.Main.Model.Question.QuestionText import QuestionText


class Party():
    def __init__(self,compteur=0,questionList=[]):
        self.id : str = self.generateRandomUrl(10);
        self.playerList : [Player] = []
        self.questionList :[question] =questionList
        self.compteur: int= compteur
        self.timeLeft = 0;
        self.generateQuestion()

    def generateRandomUrl(self,size):
        return ''.join(random.choices(string.ascii_uppercase + string.digits, k=size))

    def addPlayer(self,player):
        self.playerList.append(player)

    def getPseudo_Player_List(self):
        plist = []

        for p in self.playerList:
            print(p)
            plist.append(p.name);
        return plist;

    def sendEventToPlayer(self,eventName,json,socketio,messageReceived):
        for p in self.playerList:
            if messageReceived == None:
                socketio.emit(eventName, json, room=p.last_session_id, callback=self.ack())
            else:
                socketio.emit(eventName, jsonlib.dumps(json), callback=messageReceived,room=p.last_session_id)

    def ack(self):
        print("msg receilve")

    def compteurUp(self):
        self.compteur=self.compteur+1
    
    def compteurDown(self):
        self.compteur=self.compteur-1

    def getCurentQuestion(self):
        if len(self.questionList) >0 and self.compteur > -1 and self.compteur<=len(self.questionList):
         return self.questionList[self.compteur-1]
        else:
            return None;

    def generateQuestion(self):
       self.questionList= [QuestionText('Qui Mange des Pomme', 'Chirac'),
                           QuestionText('Qui Mange des Pomme2', 'Chirac'),
                           QuestionText('Qui Mange des Pomme3', 'Chirac')];
       self.compteur = len(self.questionList)

