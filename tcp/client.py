import socket

def send_message_to_server(host: str, port: int):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.connect((host, port))

    while True:
        message = input("Enter your message: ")
        server.sendall(message.encode())

        try:
            data = server.recv(1024)

            if not data:
                print(f"Server [{host}:{port}] is down.")
                break

            print(f"[SERVIDOR]: {data.decode()}")
        except ConnectionResetError:
            print("Conexão closed by the server.")
            break


if __name__ == "__main__":
    HOST = "localhost"
    PORT = 8000

    send_message_to_server(HOST, PORT)