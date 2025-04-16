import socketio
import eventlet

sio = socketio.Server()
app = socketio.WSGIApp(sio)

@sio.on('connect')
def connect(sid, environ):
    print(f'Клиент {sid} подключился')
    sio.emit("message", to=sid, data={'text': 'Добро пожаловать на сервер!'})

@sio.event
def disconnect(sid):
    print(f"Клиент отключился: {sid}")

# Добавляем пользователя в комнату
@sio.on("join_lobby")
def join_lobby(sid, data):
    sio.enter_room(sid, 'lobby')
    print(f'Клиент {sid} добавлен в lobby')
    sio.emit("message", {"text": f"Клиент {sid} добавлен в lobby"} )

# Получаем все комнаты пользователя
@sio.on("get_rooms")
def get_rooms(sid, data):
    result = sio.rooms(sid)
    print(f"Получаем все комнаты пользователя: {result}")
    sio.emit("message", {"text": f"Клиент {sid} находится в комнатах: {result}"})

eventlet.wsgi.server(eventlet.listen(('', 80)), app)