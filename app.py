from flask import Flask, render_template, request, redirect
from flask_socketio import SocketIO

from src.Main.Controler.Event.PartyNewPlayer import partyNewPlayerControler
from src.Main.Controler.JoinControler import JoinControler
from src.Main.Controler.LobbyControler import lobbyControler
from src.Main.Model.Game import Game
from src.Main.Model.Party import Party

import json as jsonlib
app = Flask(__name__)
app.config['SECRET_KEY'] = 'tmpKey'
socketio = SocketIO(app)
clients = []

game = Game()

@socketio.event
def connect():
    print('connection established')
    print(request.sid)
    clients.append(request.namespace)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/join')
def join():
    return render_template('join.html')

@app.route('/party/<party_id>')
def party(party_id):
    return lobbyControler(request,party_id);

#Lorsque une perssone rejoin une game
@app.route('/joinGame',methods=["GET", "POST"])
def join_game():
    return JoinControler(request,game);

#Event lorsque un joeur rejoin une partie deja existant
@socketio.on('Evt_party_join')
def ckEvt_party_join(json):
    #On rentre dans le controler qui envois une reponce
    partyNewPlayerControler(json,game,socketio,messageReceived);




def messageReceived(methods=['GET', 'POST']):
    print('message was received!!!')

@socketio.on('my event')
def handle_my_custom_event(json, methods=['GET', 'POST']):
    print('received my event: ' + str(json))
    socketio.emit('my response', json, callback=messageReceived)
    #Envoyer un message a un seul uttilisateur (grasse a sa session id)
    socketio.emit('boy', "GG boy you send a message from serveur", callback=messageReceived,room=request.sid)



if __name__ == '__main__':
    socketio.run(app, debug=True)
