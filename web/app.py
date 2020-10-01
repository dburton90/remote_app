from flask import Flask, render_template


def create_app():
    app = Flask(__name__)

    from src import streamer
    app.register_blueprint(streamer.bp)

    @app.route('/')
    def index():
        return render_template('index.html')

    return app


if __name__ == '__main__':
    create_app().run(host='0.0.0.0')
