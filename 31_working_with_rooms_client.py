import socketio
import time

# Создаем полноценного клиента
sio = socketio.Client()

# Обработчик подключения
@sio.event
def connect():
    print("Успешно подключен к серверу")

# Обработчик сообщений
@sio.on('message')
def on_message(data):
    print(f"Получено сообщение от сервера: {data}")

# Подключение
print("🔌 Подключаемся к серверу...")
sio.connect('http://0.0.0.0:80')

# Отправка событий
print("Отправляем join_lobby")
sio.emit("join_lobby", {"text": "hello"})

print("Отправляем get_rooms")
sio.emit("get_rooms", {"text": "hello"})

# Ожидаем немного, чтобы сервер успел ответить
time.sleep(2)

# Завершаем соединение
sio.disconnect()
