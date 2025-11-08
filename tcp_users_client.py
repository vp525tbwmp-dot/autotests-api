import socket

HOST = "127.0.0.1"
PORT = 12345


def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))

    client_socket.send("Привет, сервер!".encode())

    response = client_socket.recv(1024).decode()
    print(response)

    client_socket.close()


if __name__ == "__main__":
    main()
