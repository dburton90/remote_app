import os
import mouse
from flask_socketio import SocketIO, Namespace

sio = SocketIO(cors_allowed_origins="*")

@sio.on('mouse move')
def mouse_move(data):
    data.setdefault('x', 0)
    data.setdefault('y', 0)
    if not (data['x'] == data['y'] == 0):
        mouse.move(**data, absolute=False)
    print(data)


@sio.on('connect')
def on_connect(**kwargs):
    print('connect')
    print(kwargs)
    sio.emit('bravo connected', 'hura')
