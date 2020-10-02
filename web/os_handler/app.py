import os
import pyautogui
import mouse
from flask_socketio import SocketIO, Namespace

from os_handler.programs import programs

sio = SocketIO(cors_allowed_origins="*")


@sio.on('mouse move')
def mouse_move(data):
    data.setdefault('x', 0)
    data.setdefault('y', 0)
    if not (data['x'] == data['y'] == 0):
        mouse.move(**data, absolute=False)
    print(data)


@sio.on('mouse click')
def mouse_click(data):
    print('click', data)
    if data > 1:
        pyautogui.doubleClick()
    else:
        pyautogui.click()


@sio.on('program')
def on_program(data):
    print('program', data)
    try:
        program = programs[data['name']]
        action = data['action']
        action = getattr(program, action)
    except (KeyError, AttributeError):
        return
    args = data.get('args', [])
    if not isinstance(args, list):
        args = [args]
    action(*args)



@sio.on('connect')
def on_connect(**kwargs):
    print('connect')
    print(kwargs)
    sio.emit('bravo connected', 'hura')
