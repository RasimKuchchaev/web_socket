import socketio
import time

# Создаем полноценного клиента
sio = socketio.Client()

# Обработчик сообщений
@sio.on('message')
def on_message(data):
    print(f"Получено сообщение от сервера: {data.get('text')}")

@sio.on('update')
def on_message(data):
    print(f"Update от сервера: {data.get('message')}")

# Подключение
print("Подключаемся к серверу...")
sio.connect('http://0.0.0.0:80')

sio.emit('join', {'room':'roomname'})

# Удерживаем соединение
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("Отключаемся от сервера...")
    sio.disconnect()


