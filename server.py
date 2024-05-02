import socket
import time

# Define host and port
HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

# Create a socket object
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # Bind the socket to the address and port
    s.bind((HOST, PORT))
    # Listen for incoming connections
    s.listen()
    print(f"Server listening on {HOST}:{PORT}")
    # Accept connection from client
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        while True:
            # Send a message to the client
            conn.sendall(b"Hello from server\n")
            # Wait for a while before sending the next message
            time.sleep(1)
