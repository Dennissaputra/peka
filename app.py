from flask import Flask, Response,render_template,jsonify,request
import cv2
import numpy as np 


from YOLO_Video import video_detection
app = Flask(__name__)

def generate_frames(path_x = ''):
    yolo_output = video_detection(path_x)
    for detection_ in yolo_output:
        ref,buffer=cv2.imencode('.jpg',detection_)
        frame=buffer.tobytes()
        yield (b'--frame\r\n'
                    b'Content-Type: image/jpeg\r\n\r\n' + frame +b'\r\n')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/detection')
def detection():
    return render_template('deteksi.html')

@app.route('/about')
def about():
    return render_template('aboutus.html')

@app.route('/dictionary')
def dictionary():
    return render_template('dictionary.html')

@app.route('/webcam')
def webcam():
    return Response(generate_frames(path_x=0), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == "__main__":
    app.run(debug=True)