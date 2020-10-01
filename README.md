
https://mottie.github.io/Keyboard/
xdotool mousemove_relative -- -200 -100
check class for window xprop WM_CLASS 

EXPLORE_PROGRAM
xprop WM_CLASS _NET_WM_PID
class = WM_CLASS
paht = ps -o cmd -q _NET_WM_PID
i3id = i3-msg -t get_workspaces | jq '.[] | select(.focused==true).num' 


PROGRAM:
- name: Firefox
- path: /usr/lib/firefox/firefox
- classname: firefox
- i3Id: 1

WINDOWS:
exists: pgrep -f /opt/spotify/spotify
focus: i3-msg workspace number 1
focus2:  xdotool search --onlyvisible --sync --class --classname "firefox" windowactivate --sync
open: i3-msg exec firefox
open2: firefox
send key: xdotool key ctrl+t
current window name: xdotool getactivewindow getwindowname
close: pkill -f /opt/spotify/spotify

ALL:
fullscrean: ctrl+F
console: win+Enter


FIREFOX
- switching: Alt+1/2/...
- lastTab: Ctrl+Tab
- searchTab: :b
- newTab: ctrl+t
- closeTab:
- showmenutabs: F1
- reload: F5
- Go Down a Screen: Page Down
- Go Up a Screen: Page Up
- Go to Bottom of Page:	End
- Go to Top of Page: Home
- zoom + : Ctrl++
- zoom - : Ctrl+-
- search: /
    - next: F3
    - previous: Shift+F3
- find link contains text: '
- next tab: ctrl+pagedown
- previous tab: ctrl+pageup
- Esc


SPOTIFY
- search
- filter song
- move on page (TAB/ Shift+Tab)
- bakck/forward
- shuffle/repeat
pkill -x spotify
spotify --uri=spotify:playlist:1RmO97PgSlRKAH3EKPIf1n

MOVING: tab / Shift+Tab

Search: Ctrl+L
Filter: Ctrl+F
Back: Alt+<-
Forward: Alt+->
Repeat: Ctrl+R
Shuffle: Ctrl+S


STREAM DESKTOP
https://github.com/akmamun/camera-live-streaming/blob/master/app.py
ffmpg
https://trac.ffmpeg.org/wiki/Capture/Desktop
nginx
https://stackoverflow.com/questions/33254236/mpeg-dash-support-in-nginx
create stream
https://abhitronix.github.io/vidgear/gears/screengear/usage/
share stream
https://abhitronix.github.io/vidgear/gears/streamgear/usage/

```python
import sys
import pathlib

from vidgear.gears import ScreanGear
from vidgear.gears import StreamGear

if len(sys.argv) < 2:
    raise ValueError("Missing argument with path")

dir_path = pathlib.Path(sys.argv[1])

if not dir_path.exists():
    raise ValueError("Path '{}' does not exists".format(sys.argv[1]))
if not dir_path.is_dir():
    raise ValueError("Path '{}' is not dir".format(sys.argv[1]))

# open any valid video stream
stream = ScreenGear().start()

# describe a suitable manifest-file location/name
streamer = StreamGear(output=str(dir_path.joinpath("dash_out.mpd")))

# loop over
while True:

    # read frames from stream
    frame = stream.read()

    # check for frame if Nonetype
    if frame is None:
        break

    # send frame to streamer
    streamer.stream(frame)

```

show stream
https://github.com/Dash-Industry-Forum/dash.js

