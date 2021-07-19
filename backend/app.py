import atexit
import json as jsonlib
import time

from apscheduler.schedulers.background import BackgroundScheduler
from flask import Flask, redirect, render_template, request
from flask_cors import CORS
from flask_socketio import SocketIO

from backend.src.Main.Controler.Event.PartyNewPlayerControler import \
    party_new_player_controller
from backend.src.Main.Controler.Event.QuestionControler import get_question
from backend.src.Main.Controler.Event.StartGmeControler import start_game_controller
from backend.src.Main.Controler.JoinControler import join_controller
from backend.src.Main.Controler.LobbyControler import lobby_controller
from backend.src.Main.Model.Game import Game
from backend.src.Main.Model.Party import Party
from backend.src.Main.Model.Question import QuestionText
from backend.src.Main.Scheduler import next_question_party

app = Flask(__name__)
app.config['SECRET_KEY'] = 'tmpKey'
CORS(app)
socketio = SocketIO(app, cors_allowed_origins=[
    'http://localhost:5000', 'http://localhost:3000', 'http://127.0.0.1:5000', 'http://127.0.0.1:3000'])
clients = []
game = Game()
Game.currentGame = game

t = Party(3, [QuestionText.QuestionText('Qui Mange des Pomme', 'Chirac').get_json(), QuestionText.QuestionText(
    'Qui Mange des Pomme2', 'Chirac').get_json(),
              QuestionText.QuestionText('Qui Mange des Pomme3', 'Chirac').get_json()])


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
    return lobby_controller(request, party_id)


# Lorsque une perssone rejoin une game
# @app.route('/joinGame',methods=["GET", "POST"])


@socketio.on('Evt_join_game')
def join_game(json):
    return join_controller(request, json, game, socketio, messageReceived)


# Event lorsque un joeur rejoin une partie deja existant


@socketio.on('Evt_party_join')
def check_party_join(json):
    # On rentre dans le controler qui envois une reponce
    party_new_player_controller(request, json, game, socketio, messageReceived)


def messageReceived(methods=['GET', 'POST']):
    print('message was received!!!')


@socketio.on('my event')
def handle_my_custom_event(json, methods=['GET', 'POST']):
    print('received my event: ' + str(json))
    socketio.emit('my response', json, callback=messageReceived)
    # Envoyer un message a un seul uttilisateur (grasse a sa session id)
    socketio.emit('boy', "GG boy you send a message from serveur",
                  callback=messageReceived, room=request.sid)


@app.route('/test')
def question_template():
    return render_template('testQuestion.html')


@socketio.on('question')
def question_event(methods=['GET', 'POST']):
    get_question(request, None, game, socketio, messageReceived)


''' if t.compteur-1 < 0 :
        print('fin')
    else :
        socketio.emit('my question',t.questionList[t.compteur-1], callback=messageReceived)
        t.compteurDown()
'''


@socketio.on('reponse')
def reponse_event(json, methods=['GET', 'POST']):
    # print(json)
    Propa = jsonlib.loads(jsonlib.dumps(json))
    print(Propa['reponse'])


@app.route('/setting')
def configure_party():
    return render_template('configure.html')


@socketio.on('setting')
def response_event(json, methods=['GET', 'POST']):
    Propa = jsonlib.loads(jsonlib.dumps(json))
    print(str(Propa))


@socketio.on('TypeList')
def type_list():
    socketio.emit('repTypeList', str(['test', 'tesr2']))


# Action au start
@socketio.on('startGame')
def start_game(json):
    start_game_controller(request, json, game, socketio, messageReceived)


# Cette fonction vas s'execute tout les seconde


def go_to_next_question():
    next_question_party(game, socketio)


scheduler = BackgroundScheduler()
scheduler.add_job(func=go_to_next_question, trigger="interval", seconds=1)
scheduler.start()

atexit.register(lambda: scheduler.shutdown())

if __name__ == '__main__':
    socketio.run(app, debug=True)
