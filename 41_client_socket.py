import socketio

# Создание клиента сокета
sio = socketio.SimpleClient()

# Подключение к серверу
sio.connect('ws://0.0.0.0:80')