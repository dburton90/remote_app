from flask import Flask, render_template
from flask_socketio import SocketIO
from whitenoise import WhiteNoise
import pathlib
import socketio
from os_handler.app import sio

BASE = pathlib.Path(__file__).absolute().parent.parent
FRONTEND = BASE.joinpath('frontend', 'dist', 'spa')


def create_app(config='config.Default'):
    app = Flask(__name__)
    sio.init_app(app)
    socketio.WSGIApp(sio, app.wsgi_app)
    app.config.from_object(config)

    app.wsgi_app = WhiteNoise(app.wsgi_app, root=FRONTEND)

    from src import streamer
    app.register_blueprint(streamer.bp)

    from os_handler import programs
    app.register_blueprint(programs.bp)

    @app.route('/')
    def index():
        return FRONTEND.joinpath('index.html').read_text()

    sio.run(app, logger=True)
    return app


if __name__ == '__main__':
    create_app().run(host='0.0.0.0')
