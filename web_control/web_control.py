from flask import Flask
from flask import render_template, request
import RPi.GPIO as GPIO
import time
import serial
import os


app = Flask(__name__)

arduino_serial = serial.Serial(port="/dev/ttyAMA0", baudrate=9600, timeout=.1)


@app.route("/")
def index():
    return render_template('index.html')

@app.route('/left_side')
def left_side():
    data1="LEFT"
    arduino_serial.write(bytes('L', 'utf-8'))
    return 'true'

@app.route('/right_side')
def right_side():
   data1="RIGHT"
   arduino_serial.write(bytes('R', 'utf-8'))
   return 'true'

@app.route('/up_side')
def up_side():
   data1="FORWARD"
   arduino_serial.write(bytes('F', 'utf-8'))
   return 'true'

@app.route('/down_side')
def down_side():
   data1="BACK"
   arduino_serial.write(bytes('B', 'utf-8'))
   return 'true'

@app.route('/stop')
def stop():
   data1="STOP"
   arduino_serial.write(bytes('S', 'utf-8'))
   return  'true'

@app.route('/lighton')
def lighton():
   data1="LIGHTON"
   arduino_serial.write(bytes('W', 'utf-8'))
   return 'true'

@app.route('/lightoff')
def lightoff():
   data1="LIGHTOFF"
   arduino_serial.write(bytes('w', 'utf-8'))
   return  'true'

@app.route('/handwave')
def handwave():
   data1="HANDWAVE"
   arduino_serial.write(bytes('v', 'utf-8'))
   return  'true'

@app.route('/dance')
def dance():
   data1="DANCE"
   arduino_serial.write(bytes('U', 'utf-8'))
   return  'true'

@app.route('/cameraon')
def cameraon():
   data1="CAMERAON"
   os.system("/home/pi/RPi_Cam_Web_Interface/start.sh ")
   return  'true'

@app.route('/cameraoff')
def cameraoff():
   data1="CAMERAOFF"
   os.system("/home/pi/RPi_Cam_Web_Interface/stop.sh ")
   return  'true'

@app.route('/stand')
def stand():
   data1="STAND"
   arduino_serial.write(bytes('X', 'utf-8'))
   return  'true'

@app.route('/sit')
def sit():
   data1="SIT"
   arduino_serial.write(bytes('x', 'utf-8'))
   return  'true'

@app.route('/poweroff')
def poweroff():
   data1="POWEROFF"
   os.system("sudo poweroff")
   return  'true'

if __name__ == "__main__":
 print("Start")
 app.run(host='0.0.0.0',port=5010)

