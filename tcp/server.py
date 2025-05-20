import socket

def start_server(host: str, port: int):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(1)

    print(f"- Server is running at [{host}:{port}]...")

    while True:
        client_socket, client_addr = server.accept()
        print(f"- Established connection at address: {client_addr}.")

        while True:
            try:
                data = client_socket.recv(1024)

                if not data:
                    print(f"Client [{host}:{port}] disconnected.")
                    break

                print(f"[CLIENT]: {data.decode()}")
                client_socket.sendall("Message received".encode())
            except ConnectionResetError:
                print("Connection ended abruptaly")
                break

if __name__ == "__main__":
    HOST = "localhost"
    PORT = 8000

    start_server(HOST, PORT)