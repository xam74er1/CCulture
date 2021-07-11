import json

from flask import Request

from src.Main.Model.Game import Game
from src.Main.Model.Party import Party
from src.Main.Model.Player import Player
from src.Main.Model.Question.question import Question


def getQuestion(request : Request ,js,game:Game,socketio,messageReceived):

    party : Party = game.getPartyStatic()
    player : Player = game.getPlayerStatic();
    #Par secuprtie on lui remet son SID
    player.last_session_id = request.sid;
    question : Question = party.getCurentQuestion()
    #On ne renvois la question que a celui qui la demende
    socketio.emit('my question', question.get_json(), callback=messageReceived,room=player.last_session_id)
