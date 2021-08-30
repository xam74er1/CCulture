import atexit
import json as jsonlib

from apscheduler.schedulers.background import BackgroundScheduler
from flask import Flask, render_template, request
from flask_cors import CORS
from flask_socketio import SocketIO

from backend.src.Main.Controler.DisconectedControler import disconnect_controller, connect_controller
from backend.src.Main.Controler.Event.DisplayAnswerControler import displays_current_answer
from backend.src.Main.Controler.Event.PartyNewPlayerControler import \
    party_new_player_controller
from backend.src.Main.Controler.Event.QuestionControler import get_question
from backend.src.Main.Controler.Event.ResponseController import response_controller
from backend.src.Main.Controler.Event.SetCorectAswerControler import set_valid_answer
from backend.src.Main.Controler.Event.StartGameController import start_game_controller
from backend.src.Main.Controler.JoinControler import join_controller
from backend.src.Main.Controler.LobbyControler import lobby_controller
from backend.src.Main.Model.Game import Game
from backend.src.Main.Model.Party import Party
from backend.src.Main.Model.Question import QuestionText
from backend.src.Main.Model.Question.GenerateQuestion import generateQuestion
from backend.src.Main.Model.Utils.SqliteDAO import DAOConnextion
from backend.src.Main.Scheduler import next_question_party
from backend.src.Test.Controler.AutoFillPartyWithAnswer import auto_fill_party_wth_answer

app = Flask(__name__)
app.config['SECRET_KEY'] = 'tmpKey'
CORS(app)
socketio = SocketIO(app, cors_allowed_origins=[
    'http://localhost:5000', 'http://localhost:3000', 'http://127.0.0.1:5000', 'http://127.0.0.1:3000'])
clients = []
game = Game()
Game.currentGame = game
# Connextion a la bdd
DAOConnextion()

Game.currentGame.root = generateQuestion();

t = Party(3, [QuestionText.QuestionText('Qui Mange des Pomme', 'Chirac').get_json(), QuestionText.QuestionText(
    'Qui Mange des Pomme2', 'Chirac').get_json(),
              QuestionText.QuestionText('Qui Mange des Pomme3', 'Chirac').get_json()])


@socketio.event
def connect():
    print('connection established')
    connect_controller(request, None, game, socketio, messageReceived)
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


@socketio.on('disconnect')
def disconectB():
    print("Deconextion")


@socketio.event
def disconnect():
    print('disconnected from server')
    disconnect_controller(request, None, game, socketio, messageReceived)


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


@socketio.on('Evt_party_game_get_question')
def question_event():
    get_question(request, game, socketio, messageReceived)


@socketio.on('Evt_party_game_send_response')
def send_response_event(json, methods=['GET', 'POST']):
    response_controller(request, json, game, socketio, messageReceived)


@app.route('/setting')
def configure_party():
    return render_template('configure.html')


@socketio.on('setting')
def response_event(json, methods=['GET', 'POST']):
    props = jsonlib.loads(jsonlib.dumps(json))
    print(str(props))


@socketio.on('TypeList')
def type_list():
    socketio.emit('repTypeList', str(['test', 'tesr2']))


# Action au start
@socketio.on('Evt_party_start_game')
def start_game(json):
    start_game_controller(request, json, game, socketio, messageReceived)


# Lorsque le joeure a evaluer toute ses reponce il renvois
@socketio.on('Evt_party_set_valid_answers')
def get_current_answer(json):
    set_valid_answer(request, json, game, socketio, messageReceived)


# Affiche la reponse actuelle
@socketio.on('Evt_party_get_current_answer')
def get_current_answer(json):
    displays_current_answer(request, json, game, socketio, messageReceived)


# Fonction de test qui n'a pas vocaction a reste
@socketio.on('Evt_Test_fill_answer')
def fill_answer(json):
    auto_fill_party_wth_answer(request, json, game, socketio, messageReceived)


# Cette fonction vas s'execute tout les seconde
def go_to_next_question():
    next_question_party(game, socketio)


scheduler = BackgroundScheduler()
scheduler.add_job(func=go_to_next_question, trigger="interval", seconds=1)
scheduler.start()

atexit.register(lambda: scheduler.shutdown())

if __name__ == '__main__':
    socketio.run(app, debug=True)
