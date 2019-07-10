from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)

# Socketio wrapps our flask app
socketio = SocketIO(app)

# Server/Socket events

# Connection for user
@socketio.on('connect', namespace='/user')
def connect():
    print('a user connected')

# Connection for pi
@socketio.on('connect', namespace='/pi')
def connect():
    print(' a pi connected')


@socketio.on('change lights', namespace='/user')
def handle_change_lights(data):
    socketio.emit('change lights', data, namespace='/pi')
    
@socketio.on('changed lights', namespace='/pi')
def handle_changed_lights(data):
    socketio.emit('changed lights', {'val': 'Changed to ' + data['val']}, namespace='/user')

# Routing
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    socketio.run(app)
