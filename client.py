import socket

# Define host and port
HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

# Create a socket object
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # Connect to the server
    s.connect((HOST, PORT))
    # Receive messages from the server indefinitely
    while True:
        data = s.recv(1024)  # Receive up to 1024 bytes of data
        if not data:
            break
        print("Received:", data.decode())
