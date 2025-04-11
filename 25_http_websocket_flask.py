import eventlet
from flask import Flask
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
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Socket.IO</title>
        <script src="https://cdn.socket.io/4.7.2/socket.io.min.js"></script>
    </head>
    <body>
        <h1>Socket.IO клиент</h1>
        <ul id="messages"></ul>
        <script>
            const socket = io();

            socket.on('connect', () => {
                const li = document.createElement("li");
                li.textContent = "✅ Подключено к серверу";
                document.getElementById("messages").appendChild(li);
            });

            socket.on('disconnect', () => {
                const li = document.createElement("li");
                li.textContent = "❌ Отключено от сервера";
                document.getElementById("messages").appendChild(li);
            });

            socket.on('message', (msg) => {
                const li = document.createElement("li");
                li.textContent = msg;
                document.getElementById("messages").appendChild(li);
            });
        </script>
    </body>
    </html>
    """

eventlet.wsgi.server(eventlet.listen(('127.0.0.1', 80)), app)