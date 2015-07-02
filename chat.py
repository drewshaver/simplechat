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
    emit('register population', broadcast=True)

@socketio.on('register me')
def register_one(username):
    join_room(username)
    emit('register one', username, broadcast=True)

#TODO use rooms so messages aren't public
@socketio.on('message')
def send_message(data):
    emit('message', data, room=data['recipient'])
    emit('message', data, room=data['from'])

#TODO disconnect

#TODO can message yourself?

#TODO sanitize usernames / make sure they are encoded safely

if __name__ == '__main__':
    socketio.run(app)
