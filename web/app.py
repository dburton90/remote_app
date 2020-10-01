from time import sleep, time

from flask import Flask, render_template, Response
import cv2
import mss
import numpy

from vidgear.gears import ScreenGear

# open any valid video stream

app = Flask(__name__)

def gen_frames(width=640, monitor=1, fps=30):  # generate frame by frame from camera
    with mss.mss() as sct:
        monitor = sct.monitors[monitor]
        height = int(round((width / monitor['width']) * monitor['height'], 0))
        sleep_fps = 1/fps
        while(True):
            frame =  sct.grab(monitor)
            if frame is None:
                break
            # frame = mss.tools.to_png(frame.rgb, size=(width, height))
            frame = numpy.array(frame)
            frame = cv2.resize(frame, dsize=(width, height), interpolation=cv2.INTER_CUBIC)
            _, frame = cv2.imencode('.png', frame)
            frame = frame.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/png\r\n\r\n' + frame + b'\r\n')  # concat frame one by one and show result
            sleep(sleep_fps)



@app.route('/video_feed')
def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(gen_frames(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/')
def index():
    """Video streaming home page."""
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0')
