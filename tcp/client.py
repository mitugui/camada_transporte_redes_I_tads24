import socket

def send_message_to_server(host: str, port: int):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.connect((host, port))

    while True:
        message = input("Digite a mensagem: ")
        server.sendall(message.encode())

        data = server.recv(1024).decode()
        print(f"[SERVIDOR]: {data}")

if __name__ == "__main__":
    HOST = "localhost"
    PORT = 8000

    send_message_to_server(HOST, PORT)