import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('192.168.X.XX', 65234))

name = input("Insert your name: ")

while True:
    message = input(f"{name} -> ")
    client.send(f"{name} -> {message}".encode())
