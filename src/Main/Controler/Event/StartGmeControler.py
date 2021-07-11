from flask import Request, render_template

from src.Main.Model import Game
from src.Main.Model.Party import Party


def startGameContoroler(request : Request ,json,game:Game,socketio,messageReceived):
    print("Start game")
    party : Party = game.getPartyStatic()
    game.addPartyStart(party)
    jsonToReturn = render_template('testQuestion.html');
    party.sendEventToPlayer("partyStart",jsonToReturn,socketio,messageReceived);