from src.Main.Model.Player import Player
import string
import random # define the random module


class Party():
    def __init__(self):
        self.id : str = self.generateRandomUrl(10);
        self.playerList : [Player] = []

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