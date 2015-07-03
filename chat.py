from flask import Flask
from flask import render_template
from flask.ext.socketio import SocketIO, emit, join_room

app = Flask(__name__)
app.config['SECRET_KEY'] = 'TODO'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

#TODO better way to do simple forwarding?
@socketio.on('request population')
def request_population():
    emit('request population', broadcast=True)

@socketio.on('register me')
def register_one(username):
    join_room(username)
    emit('register one', username, broadcast=True)

@socketio.on('deregister me')
def deregister_one(username):
    emit('deregister one', username, broadcast=True)

@socketio.on('message')
def send_message(data):
    #TODO can we check for receipt before confirming to sender?
    emit('message', data, room=data['recipient'])
    
    # Could have recorded this on the front end, but this way
    # we at least have confirmation that it got to the server
    emit('message', data, room=data['from'])

#TODO sanitize usernames / make sure they are encoded safely

if __name__ == '__main__':
    socketio.run(app)
