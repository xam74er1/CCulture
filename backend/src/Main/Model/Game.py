from flask import session, request

from backend.src.Main.Model.Party import Party
from backend.src.Main.Model.Player import Player
from backend.src.Main.Model.Question.QuestionTree.QuestionTree import QuestionTree


class Game:
    currentGame = None

    def __init__(self):
        self.id = 0
        self.listParty: [Party] = []
        self.listPlayer: [Player] = []
        self.listRunningParty: [Party] = []  # Liste de toute les partie qui son en cour avec des question qui doive etre affiche les une apres les autre
        self.root : QuestionTree = None #Arbre pertant de ger toute les question

    def add_player(self, player: Player):
        self.listPlayer.append(player)

    def add_party(self, party: Party):
        self.listParty.append(party)

    def add_party_start(self, party: Party):
        self.listRunningParty.append(party)

    def remove_party(self, party: Party):
        self.listRunningParty.remove(party)

    def get_party(self, party_id: str):
        for p in self.listParty:
            if p.id == party_id:
                return p
        return None

    def get_player_from_uuid(self, uuid: str):
        #if len(self.listPlayer) > 0:
            #print("Player list  " + str(self.listPlayer[0].uuid))
        for p in self.listPlayer:
            #print(p.uuid)
            if str(p.uuid) == str(uuid):
                return p
        return None

    def get_player_name_list(self, id_party):
        party: Party = self.get_party(id_party)
        return party.get_pseudo_player_list()

    @staticmethod
    def get_game():
        return Game.currentGame

    @staticmethod
    def get_player_static():
        game: Game = Game.currentGame
        tmp = None;
        if session.get("uuid") :
            tmp: Player = game.get_player_from_uuid(session["uuid"])
        if tmp is None:
            tmp = game.get_player_from_uuid(request.cookies["userID"])
            session["uuid"] = tmp.uuid
        return tmp

    @staticmethod
    def get_party_static():
        game: Game = Game.currentGame
        player: Player = game.get_player_static()
        if player is None:
            print("Player not found")

        return game.get_party(player.current_party_id)
