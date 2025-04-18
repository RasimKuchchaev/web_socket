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

# Отправить сообщение в комнате
@sio.on("brоadcast_lobby")
def my_message(sid, data):
    # Отправить сообщение всем в комнате
    sio.emit('message', "hello to everyone in lobby", room='lobby')
    # Отправить сообщение всем в комнате кроме себя
    sio.emit('message', "hello to everyone in lobby", room='lobby', skip_sid=sid)

# Покинуть комнату
@sio.on("leave_lobby")
def exit_chat(sid, data):
    sio.leave_room(sid, 'lobby')
    sio.emit('message', "!!!!!! leave_lobby !!!!!!", room='lobby', skip_sid=sid)
    print("!!!!!! leave_lobby !!!!!!")

# Удалить комнату и всех выгнать
@sio.on("close_room")
def close_room(sid, data):
    sio.close_room("lobby")
    sio.emit('message', "!!!!!! close_room !!!!!!", to=sid)
    print("!!!!!! close_room !!!!!!")

eventlet.wsgi.server(eventlet.listen(('', 80)), app)