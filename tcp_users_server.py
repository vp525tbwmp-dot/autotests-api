import socket

HOST = "127.0.0.1"
PORT = 12345
messages = []


def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen(10)
    print(f"TCP-сервер запущен на {HOST}:{PORT}")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Пользователь с адресом: {client_address} подключился к серверу")

        data = client_socket.recv(1024).decode()
        if data:
            print(f"Пользователь с адресом: {client_address} отправил сообщение: {data}")

            messages.append(data)
        history = "\n".join(messages)
        client_socket.send(history.encode())
        client_socket.close()


if __name__ == "__main__":
    main()
