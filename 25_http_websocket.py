import eventlet
import socketio

# Путь к статике
static_files = { '/': 'index.html' }

sio = socketio.Server(cors_allowed_origins='*', async_mode='eventlet')

app = socketio.WSGIApp(sio, static_files=static_files)

@sio.event
def connect(sid, environ):
    print(f"Пользователь {sid} подключился")

@sio.event
def disconnect(sid):
    print(f"Пользователь {sid} отключился")

eventlet.wsgi.server(eventlet.listen(('0.0.0.0', 80)), app)