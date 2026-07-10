import socket
import threading

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("0.0.0.0", 5000))
server.listen()

clients = []
names = []

print("Server running on port 5000...")

def broadcast(message, sender=None):
    for client in clients[:]:
        if client != sender:
            try:
                client.send(message)
            except:
                if client in clients:
                    index = clients.index(client)
                    clients.remove(client)
                    names.pop(index)

def handle_client(conn, addr):
    try:
        conn.send("NAME".encode())
        name = conn.recv(1024).decode().strip()

        clients.append(conn)
        names.append(name)

        print(f"{name} joined from {addr}")
        broadcast(f"{name} joined the chat".encode(), conn)

        while True:
            msg = conn.recv(1024)
            if not msg:
                break

            text = msg.decode()
            broadcast(f"{name}: {text}".encode(), conn)

    except:
        pass

    # cleanup on disconnect
    if conn in clients:
        index = clients.index(conn)
        clients.remove(conn)
        left_name = names.pop(index)
        broadcast(f"{left_name} left the chat".encode())

    conn.close()

def receive():
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()

receive()