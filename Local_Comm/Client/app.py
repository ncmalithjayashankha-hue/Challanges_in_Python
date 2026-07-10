import socket
import threading

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("192.168.8.100", 5000))

name = input("Enter your name: ")

def receive():
    while True:
        try:
            msg = client.recv(1024).decode()

            if msg == "NAME":
                client.send(name.encode())
            else:
                print(msg)
        except:
            print("Disconnected")
            break

def send():
    while True:
        msg = input()
        full_msg = f"{name}: {msg}"
        client.send(full_msg.encode())

threading.Thread(target=receive, daemon=True).start()
threading.Thread(target=send, daemon=True).start()

while True:
    pass