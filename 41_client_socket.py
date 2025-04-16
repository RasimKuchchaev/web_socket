import socketio

# Создание клиента сокета
sio = socketio.SimpleClient()

# Подключение к серверу
print("Подключаемся к серверу")
sio.connect('ws://0.0.0.0:80')

print("Ждем и получаем ответ сервера")
event, data = sio.receive()
print(f"{event} {data}")

print("Отправляем сообщение")
sio.emit("send_message", {"text": "hello"})
event, data = sio.receive()
print("Получаем сообщение")
print(f"{event} {data}")