from src.Main.Model.Party import Party
from src.Main.Model.Player import Player


class Game:
    def __init__(self):
        self.id = 0;
        self.listParty : [Party] = []
        self.listPlayer : [Player] = [];

    def addPlayer(self,player : Player):
        self.listPlayer.append(player)

    def addParty(self,party:Party):
        self.listParty.append(party)

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