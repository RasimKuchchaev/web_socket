import eventlet
import socketio

users_count = []
# Создаем экземпляр синхронного сервера Socket.IO
sio = socketio.Server()

# Создаем WSGI приложение и связываем его с Socket.IO
app = socketio.WSGIApp(sio)

# Обработчик события подключения
@sio.event
def connect(sid, environ):
    users_count.append(sid)
    print(f"Клиент {sid} подключен")

# Обработчик события отключения
@sio.event
def disconnect(sid):
    users_count.remove(sid)
    print(f"Клиент {sid} отключен")


# Обработка событий message
@sio.on("message")
def incoming_message(sid, data):
    print("мне сказали", data, sid)


@sio.on('get_users_online')
def get_user_all(sid, data):
    online_users = len(users_count)
    print(f"online users: {online_users}  {sid}")
    sio.emit("users", {"online": online_users})


# Запускаем eventlet веб-сервер
eventlet.wsgi.server(eventlet.listen(('127.0.0.1', 8080)), app)