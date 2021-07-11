from flask import session

from src.Main.Model.Party import Party
from src.Main.Model.Player import Player


class Game:
    curentGame  = None
    def __init__(self):
        self.id = 0;
        self.listParty : [Party] = []
        self.listPlayer : [Player] = [];
        self.listRuningParty :[Party] = [] #Liste de toute les partie qui son en cour avec des question qui doive etre affiche les une apres les autre

    def addPlayer(self,player : Player):
        self.listPlayer.append(player)

    def addParty(self,party:Party):
        self.listParty.append(party)
    def addPartyStart(self,party:Party):
        self.listRuningParty.append(party)

    def removeParty(self,party:Party):
        self.listRuningParty.remove(party)

    def getParty(self,party_id : str):
        for p  in self.listParty:
            if(p.id == party_id):
                return p
        return None;
    def getPlayerFromUUID(self,uuid : str):
        print("Player list size "+str(len(self.listPlayer)))
        for p in self.listPlayer:
            print(p.uuid)
            if str(p.uuid)==str(uuid):
                return p;
        return None;

    def getPlayer_Name_List(self,idparty):
        party : Party = self.getParty(idparty);
        return party.getPseudo_Player_List();

    @staticmethod
    def getGame():
        return Game.curentGame

    @staticmethod
    def getPlayerStatic():
       game :Game = Game.curentGame
       return game.getPlayerFromUUID(session["uuid"])

    @staticmethod
    def getPartyStatic():
        game: Game = Game.curentGame
        print("Session uuid"+str(session))
        player : Player = game.getPlayerFromUUID(session["uuid"])
        print("player party id "+str(player.curent_party_id)+"|")
        return game.getParty(player.curent_party_id)


