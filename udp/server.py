import socket
 
def start_server(host:str, port:int):
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    server.bind((host, port))
    print(f"Server startou em {host}:{port}\nEscutando agora...")

    clients = set()

    while True:
        data, addr = server.recvfrom(1024)
        
        if addr not in clients:
            clients.add(addr)
            print(f"{clients}")        

        for client in clients:
            if addr != client:
                server.sendto(data, client)
            if addr == client:
                server.sendto(''.encode(), client)

if __name__=='__main__':
    HOST = 'localhost'
    PORT = 8000
    
    start_server(HOST, PORT)