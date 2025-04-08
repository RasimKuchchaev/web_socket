import eventlet
import socketio

# Создаем экземпляр синхронного сервера Socket.IO
sio = socketio.Server()

# Создаем WSGI приложение и связываем его с Socket.IO
app = socketio.WSGIApp(sio)

# Обработчик события подключения
@sio.event
def connect(sid, environ):
    print(f"Клиент {sid} подключен")

# Обработчик события отключения
@sio.event
def disconnect(sid):
    print(f"Клиент {sid} отключен")

# Запускаем eventlet веб-сервер
eventlet.wsgi.server(eventlet.listen(('127.0.0.1', 8080)), app)