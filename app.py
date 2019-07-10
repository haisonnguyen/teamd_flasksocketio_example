from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)


socketio = SocketIO(app)

# Server/Socket events

@socketio.on('connect')
def handle_connection():
    print('\nNew connection\n')

@socketio.on('custom')
def handle_custom(data):
    print('\nMessage from socket: ' + data['msg'] + '\n')
    socketio.emit('custom received', {'msg': 'The event was received!'})

@socketio.on('change lights')
def handle_change_lights(data):
    print('Changing lights to ' + data['val'])
# Routing
@app.route('/')
def hello():
    return render_template('index.html')

if __name__ == '__main__':
    socketio.run(app)
