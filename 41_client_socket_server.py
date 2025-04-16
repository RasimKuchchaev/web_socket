import socketio
import eventlet
from loguru import logger

sio = socketio.Server()
app = socketio.WSGIApp(sio)

@sio.on('connect')
def connect(sid, environ):
    logger.info(f'Клиент {sid} подключился')
    sio.enter_room(sid, 'lobby')
    logger.info(f'Клиент {sid} добавлен в lobby')
    sio.emit('message', to=sid, data={'text': 'Добро пожаловать в lobby!'})

@sio.event
def disconnect(sid):
    logger.info(f"Клиент отключился: {sid}")

# Обработчик для отправки сообщения в комнату
@sio.on('send_message')
def send_message(sid, data):
    text = data.get('text')
    sio.emit('message', {'text': text}, room="lobby")

eventlet.wsgi.server(eventlet.listen(('', 80)), app)