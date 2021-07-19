from flask import Flask, render_template, request
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'tmpKey'
socketio = SocketIO(app)
clients = []

@socketio.event
def connect():
    print('connection established')
    print(request.sid)
    clients.append(request.namespace)

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
