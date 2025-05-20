import socket

def start_server(host: str, port: int):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(1)

    print(f"- Server is running at [{host}:{port}]...")

    client_socket, client_addr = server.accept()
    print(f"- Established connection at address: {client_addr}.")

    while True:
        data = client_socket.recv(1024).decode()
        print(f"[CLIENT]: {data}")

        client_socket.sendall("pong".encode())

if __name__ == "__main__":
    HOST = "localhost"
    PORT = 8000

    start_server(HOST, PORT)