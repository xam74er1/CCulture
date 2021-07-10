from src.Main.Model.Player import Player
from src.Main.Model.Question import question
import string
import random # define the random module
import json as jsonlib


class Party():
    def __init__(self,compteur=0,questionList=[]):
        self.id : str = self.generateRandomUrl(10);
        self.playerList : [Player] = []
        self.questionList :[question] =questionList
        self.compteur: int= compteur
        self.timeLeft = 0;

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
         socketio.emit(eventName, jsonlib.dumps(json), callback=messageReceived,room=p.last_session_id)
    
    def compteurUp(self):
        self.compteur=self.compteur+1
    
    def compteurDown(self):
        self.compteur=self.compteur-1