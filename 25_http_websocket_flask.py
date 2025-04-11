import eventlet
from flask import Flask, send_from_directory
import socketio

sio = socketio.Server()

# Создаем экземпляр Flask приложения
flask_app = Flask(__name__)

app = socketio.WSGIApp(sio, flask_app)

@sio.event
def connect(sid, environ):
    print(f"Пользователь {sid} подключился")

@sio.event
def disconnect(sid):
    print(f"Пользователь {sid} отключился")

@flask_app.route("/")
def page_index():
    return send_from_directory(".", "index.html")

eventlet.wsgi.server(eventlet.listen(('127.0.0.1', 80)), app)