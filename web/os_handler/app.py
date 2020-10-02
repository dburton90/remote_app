from flask_socketio import SocketIO, Namespace

sio = SocketIO(cors_allowed_origins="*")


@sio.on('test')
def test(sid, data):
    print('test called')
    print(sid)
    print(data)
    sio.emit('bravo test', 'hura')


@sio.on('connect')
def on_connect(**kwargs):
    print('connect')
    print(kwargs)
    sio.emit('bravo connected', 'hura')
