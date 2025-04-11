import socketio

# Создаём клиент Socket.IO
sio = socketio.Client()

# Обработчик подключения
@sio.event
def connect():
    print("✅ Подключено к серверу")

# Обработчик отключения
@sio.event
def disconnect():
    print("❌ Отключено от сервера")

# Обработчик входящих сообщений
@sio.on('message')
def handle_message(data):
    if isinstance(data, dict):
        print("📥 Сообщение (dict):", data)
    else:
        print("📥 Сообщение:", data)

# Подключение к серверу
if __name__ == '__main__':
    try:
        sio.connect("http://localhost:5000", transports=["websocket"])
        sio.wait()
    except Exception as e:
        print("Ошибка подключения:", e)
