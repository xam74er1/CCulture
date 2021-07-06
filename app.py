from os import pardir
from typing import Text
from flask import Flask, render_template, request, jsonify
from flask_socketio import SocketIO
from src.Main.Model.Question import question,questionText
import json

#|- SETTING -|
app = Flask(__name__)
app.config['SECRET_KEY'] = 'tmpKey'
socketio = SocketIO(app)
clients = []
t=0

@socketio.event
def connect():
    print('connection established')
    print(request.sid)
    clients.append(request.namespace)

@app.route('/test')
def QuestionTemplate():
    return render_template('testQuestion.html')

@socketio.on('question')
def questionEvent(methods=['GET', 'POST']):
    listQ=[questionText.questionText('Qui Mange des Pomme','Chirac').get_json(),questionText.questionText('Qui Mange des Pomme2','Chirac').get_json()]
    socketio.emit('my question',listQ[1], callback=messageReceived)
    #socketio.emit('my question',question.question(1,'test').get_json(), callback=messageReceived)

@socketio.on('reponse')
def reponseEvent(json, methods=['GET', 'POST']):
    print(json)

@app.route('/')
def hello_world():
    return render_template('index.html')

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
