# import socketio
import eventlet
import eventlet.wsgi

import RPi.GPIO as GPIO
from gpiozero import Motor, OutputDevice
from time import sleep

from flask import Flask, request, send_from_directory
# from flask import Flask, render_template
from flask_socketio import SocketIO

# sio = socketio.Server()
sio = SocketIO(app)
app = Flask(__name__)

motor1 = Motor(24, 27)
motor1_enable = OutputDevice(5, initial_value=1)
# motor2 = Motor(6, 22)
# motor2_enable = OutputDevice(17, initial_value=1)
motor3 = Motor(23, 16)
motor3_enable = OutputDevice(12, initial_value=1)
motor4 = Motor(13, 18)
motor4_enable = OutputDevice(25, initial_value=1)

@app.route('/<path:path>', methods=['POST', 'GET'])
def serve_page(path):
  return send_from_directory('static', path)

@socketio.on('json')
def handle_json(json):
    print('received json: ' + str(json))

@sio.on('connect')
def connect(sid, data):
    # print("connected ", data, sid)
    sio.emit('room', room=sid)

@sio.on('robot-forward')
def message(sid):
    # Turn the motor on
    motor1.value = 1 # half speed forwards
    motor3.value = 1 # half speed forwards
    motor4.value = 1 # half speed forwards
    print('robot-forward ', str(sid))
    sio.emit('pipony moved', sid)

@sio.on('robot-back')
def message(sid):
    motor1.value = -1 # half speed backwards
    motor3.value = -1 # half speed backwards
    motor4.value = -1 # half speed backwards
    print('robot-back ', sid)

@sio.on('robot-right')
def message(sid):
    # Stop the motor by 'turning off' the enable GPIO pin
    motor1.value = 1 # right
    motor3.value = 0.5 # right
    motor4.value = 0.5 # right
    print('robot-right ', sid)

@sio.on('robot-left')
def message(sid):
    # Stop the motor by 'turning off' the enable GPIO pin
    motor1.value = .5 # left
    motor3.value = 1 # left
    motor4.value = 1 # left
    print('robot-left ', sid)

@sio.on('robot-stop')
def message(sid):
    # Stop the motor by 'turning off' the enable GPIO pin
    motor1.value = 0 # stop
    motor3.value = 0 # stop
    motor4.value = 0 # stop
    print('robot-stop ', sid)


@sio.on('disconnect')
def disconnect(sid):
    GPIO.cleanup()
    print('disconnect ', sid)

def main():
    print(' ')

if __name__ == '__main__':
    # wrap Flask application with engineio's middleware
    app = socketio.Middleware(sio, app)

    # deploy as an eventlet WSGI server
    eventlet.wsgi.server(eventlet.listen(('', 8000)), app)
    try:
        main()
    except KeyboardInterrupt:
        pass
    finally:
        GPIO.cleanup()
