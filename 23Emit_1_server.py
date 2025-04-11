import socketio
import eventlet
import logging
from flask import Flask, send_from_directory

# Настройка логов
logging.basicConfig(level=logging.INFO)

# Создаём Flask-приложение для обслуживания статики
app = Flask(__name__)

# Создаём сервер Socket.IO
sio = socketio.Server(async_mode='eventlet')

# Встраиваем Socket.IO сервер в Flask-приложение
app.wsgi_app = socketio.WSGIApp(sio, app.wsgi_app)

# Роут для отдачи HTML файла
@app.route('/')
def index():
    return send_from_directory('.', 'client.html')

# Событие подключения клиента
@sio.event
def connect(sid, environ):
    logging.info(f"Клиент подключился: {sid}")

    # видят все клиенты
    sio.emit("message", f"Пользователь присоединился {sid}")

    # видит только клиент room=sid
    sio.emit("message", f"Добро пожаловать на сервер! {sid}", room=sid)

    # видит все кроме клиента skip_sid=sid
    sio.emit("message", skip_sid=sid, data="Приветствуем нового пользователя он не видить это сообщение")

# Событие отключения клиента
@sio.event
def disconnect(sid):
    logging.info(f"Клиент отключился: {sid}")
    sio.emit("message", "Пользователь отключился")

# Запуск сервера
if __name__ == '__main__':
    logging.info("Сервер запущен на http://localhost:5000")
    eventlet.wsgi.server(eventlet.listen(('0.0.0.0', 5000)), app)
