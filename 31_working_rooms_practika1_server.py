import socketio
import eventlet

sio = socketio.Server()
app = socketio.WSGIApp(sio)

@sio.on('connect')
def connect(sid, environ):
    print(f'Клиент {sid} подключился')
    sio.emit("message", to=sid, data={'text': 'Добро пожаловать на сервер!'})
    sio.enter_room(sid, "lobby")
    sio.emit("update", {"message":"user_joined"}, room="lobby",skip_sid=sid)

@sio.event
def disconnect(sid):
    print(f"Клиент отключился: {sid}")

# список комнат и их участники sio.manager.rooms.get('/', {})
@sio.on('join')
def add_room(sid, data):
    room_info = {}

    name_room = data.get('room')
    sio.enter_room(sid, name_room)

    all_rooms = sio.manager.rooms.get('/', {})
    for room, member in all_rooms.items():
        if room==None or room==list(member)[0]:
            continue
        room_info[room] = list(member)
    print(room_info)

    for room, member in room_info.items():
        print(room, member)
eventlet.wsgi.server(eventlet.listen(('', 80)), app)