from subprocess import run

from flask import Blueprint, jsonify

bp = Blueprint('os-handler', __name__, url_prefix='/os-handler')


class Key:

    def __init__(self, name, keys=None, optional_keys=None, icon=None):
        self.name = name
        self.keys = keys
        self.optional_keys = optional_keys
        self.icon = icon

    def to_dict(self):
        return {
            'name': self.name,
            'keys': self.keys,
            'options': self.optional_keys,
            'icon': self.icon,
        }


OS = [Key('esc', ['esc']),
      Key('full-screen', ['winleft', 'f']),
      Key('tab', ['tab']),
      Key('space', ['space']), ]


class Program:
    def __init__(self, name, path, w_class, i3workspace=None, arguments=None, icon=None, keys=None):
        self.name = name
        self.path = path
        self.w_class = w_class
        self.i3workspace = i3workspace

        self.arguments = arguments
        self.icon = icon
        self.keys = {key: key.name for key in keys or []}

    def _isi3(self):
        return self.i3workspace is not None

    def _running(self):
        return len(run(['pgrep', '-f', self.path], capture_output=True).stdout) != 0

    def run(self, *arguments):
        if not self._isi3():
            return
        return run(['i3-msg', 'exec', self.path, *arguments], capture_output=True).stdout.decode()

    def focus(self):
        if not self._isi3():
            return
        if not self._running():
            self.run()
        run(['i3-msg', 'workspace', 'number', str(self.i3workspace)])

    def close(self):
        return run(['pkill', '-f', self.path], capture_output=True).stdout.decode()

    def to_dict(self):
        return {
            'name': self.name,
            'icon': self.icon,
            'keys': [k.to_dict() for k in self.keys]
        }


class Spotify(Program):
    def __init__(self, playlists=None, keys=None):
        super().__init__('spotify', '/opt/spotify/spotify', 'spotify', 8, ['--uri='], icon=None, keys=keys)
        self.playlists = playlists or {}

    def change_playlist(self, playlist):
        p = self.playlists.get(playlist, playlist)
        self.close()
        self.run('--uri=' + str(p))


"""
 32 - switching: Alt+1/2/...
 31 - lastTab: Ctrl+Tab
 30 - searchTab: :b
 29 - newTab: ctrl+t
 28 - closeTab:
 27 - showmenutabs: F1
 26 - reload: F5
 25 - Go Down a Screen: Page Down
 24 - Go Up a Screen: Page Up
 23 - Go to Bottom of Page: End
 22 - Go to Top of Page: Home
 21 - zoom + : Ctrl++
 20 - zoom - : Ctrl+-
 19 - search: /
 18     - next: F3
 17     - previous: Shift+F3
 16 - find link contains text: '
 15 - next tab: ctrl+pagedown
 14 - previous tab: ctrl+pageup
 13 - Esc
"""

programs = {p.name: p
            for p in [
                Program('firefox', '/usr/lib/firefox/firefox', 'firefox', 1,
                        keys=[
                            Key('switch', ['alt'], ['1-9'], None),
                            Key('netflix', ['alt'], ['1'], None),
                            Key('youtube', ['alt'], ['2'], None),
                            Key('lastTab', ['ctrl', 'tab']),
                            Key('nextTab', ['ctrl', 'pagedown']),
                            Key('previousTab', ['ctrl', 'pageup']),
                            Key('closeTab', ['ctrl', 'w']),
                            Key('tabs', ['f1']),
                            Key('reload', ['f5']),
                            Key('down', ['pagedown']),
                            Key('up', ['pageup']),
                            Key('top', ['home']),
                            Key('zoom +', ['ctrl', '+']),
                            Key('zoom -', ['ctrl', '-']),
                            Key('search', ['/']),
                            Key('find link', ["'"]),
                            Key('search next', ['f3']),
                            Key('previous next', ['shift', 'f3']),
                        ]),
                Spotify(),
            ]}


@bp.route('/programs')
def get_programs():
    p = {k: p.to_dict() for k, p in programs.items()}
    return jsonify({'programs': p})


@bp.route('/default-keys')
def default_keys():
    return jsonify({'defaultKeys': {k.name: k.to_dict() for k in OS}})
