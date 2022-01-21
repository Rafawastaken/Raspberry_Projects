import socket
import threading

# Substituir por IP do raspberry
HOST = "ip_servidor"
PORT = 9999

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

clients = []
nicknames = []


def broadcast(message):
    for client in clients:
        client.send(message)


def handle(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)

        except:
            index = client.index(client)
            clients.remove(client)
            client.close()

            nickname = nickname[index]
            nicknames.remove(nickname)

            broadcast(f"{nickname} - Saio do Chat!".encode('ascii'))


def receive():
    while True:
        client, addr = server.accept()
        print(f"Nova Conexao: {str(addr)}")

        client.send('NICK: '.encode('ascii'))
        nickname = client.recv(1024).decode('ascii')
        nicknames.append(nickname)
        clients.append(client)

        print(f"Nickname of client: {nickname}")
        broadcast(f"{nickname} entrou no chat!".encode('ascii'))
        client.send("Conectado".encode("ascii"))

        # Start Threading
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()


def main():
    print("Server is running...")
    receive()


if __name__ == '__main__':
    main()
