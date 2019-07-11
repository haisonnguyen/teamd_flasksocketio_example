import socketio

# Initiate socket client
socket = socketio.Client()


# Socket event handlers
@socket.on('connect', namespace='/pi')
def handle_connect():
    print('Connection to server established')

@socket.on('change lights', namespace='/pi')
def handle_change_lights(data):
    print('Received request from server: ' + data['val'])
    '''
    Place code to change lights here
    '''
    socket.emit('changed lights', data, namespace='/pi')

@socket.on('disconnect', namespace='/pi')   
def handle_disconnect():
    print('disconnected from server')

# Establish connection to server
socket.connect('http://localhost:5000', namespaces=['/pi'])
