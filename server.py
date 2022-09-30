import socket
from time import sleep

# Create and Bind server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((socket.gethostbyname(socket.gethostname()), 65234))

# Get users
server.listen()
conn, address = server.accept()

# Print users
print(f"Connection from {address[0]} with port {address[1]}")

while True:
    try: # Try getting data
        data = conn.recv(1024).decode()
        print(data)
    except ConnectionResetError: # If user leave program will close in 5 seconds
        print("User has left the chat\nEnding in 5 seconds");sleep(5)
        break