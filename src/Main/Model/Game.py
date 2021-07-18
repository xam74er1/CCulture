from flask import session, request

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
        if len(self.listPlayer)>0:
            print("Player list  "+str(self.listPlayer[0].uuid))
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
       tmp : Player = game.getPlayerFromUUID(session["uuid"])
       if tmp ==None:
        tmp =game.getPlayerFromUUID(request.cookies["userID"])
        session["uuid"] = tmp.uuid
       return tmp

    @staticmethod
    def getPartyStatic():
        game: Game = Game.curentGame
        player : Player = game.getPlayerStatic()
        if player == None:
            print("Player not found")

        return game.getParty(player.curent_party_id)


