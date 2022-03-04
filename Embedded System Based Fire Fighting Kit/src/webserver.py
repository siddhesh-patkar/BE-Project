from flask import Flask,render_template, Response,url_for,request,redirect,make_response
from FireFighterVision import VideoCamera
import json
from time import time
from sensorData import sensorData
from sendMail import sendMail

#initiate flask app
app = Flask(__name__)

#render Home page template 
@app.route('/home')
def home():
    return render_template('applicationPage.html')

#render Login page template
@app.route('/',methods=["GET","POST"])
def index():
    error = None
    if request.method == "POST":
        if request.form['username']!= "admin" or request.form['password'] != "admin":
            error = "Invalid credentials"
        else:
            return redirect(url_for('home'))
    return render_template('loginPage.html',error=error)


#get HR data in the flask server for plotting
@app.route('/HRdata', methods=["GET", "POST"])
def HRdata():
    HRdata = [time() * 1000,sensorData.HeartRate()]
    response = make_response(json.dumps(HRdata))
    response.content_type = 'application/json'
    return response

#get DHT22 data in the flask server for plotting
@app.route('/DHT22data', methods=["GET", "POST"])
def DHT22data():
    DHT22data = [time() * 1000,sensorData.HeartRate()]
    response = make_response(json.dumps(DHT22data))
    response.content_type = 'application/json'
    return response


def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

#feeding video to flask app
@app.route('/video_feed')
def video_feed():
    return Response(gen(VideoCamera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

#main 
if __name__ == '__main__':
    app.run(host="192.168.0.103",port = 5000, debug=True)
    sendMail()
