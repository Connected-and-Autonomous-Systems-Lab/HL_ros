from pynput import keyboard
import hl2ss
import socket
import time
from colorama import init, Fore
import struct

# Initialize colorama
init()

# HoloLens address
file_path = 'ip_address.txt'  # Replace 'your_file.txt' with the path to your file
with open(file_path, 'r') as file:
    # Read the content of the file
    host = file.read()

# Define host and port
HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

# Port
port = hl2ss.StreamPort.SPATIAL_INPUT
#------------------------------------------------------------------------------

client = hl2ss.rx_si(host, port, hl2ss.ChunkSize.SPATIAL_INPUT)
client.open()

def on_press(key):
    global enable
    enable = key != keyboard.Key.esc
    return enable

enable = True
# Create a socket object
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # Bind the socket to the address and port
    s.bind((HOST, PORT))
    # Listen for incoming connections
    s.listen()
    print(Fore.GREEN + f"Server listening on {HOST}:{PORT}")
    # Accept connection from client
    conn, addr = s.accept()
    with conn:
        print(Fore.GREEN + f"Connected by {addr}")

        while (enable):
            data = client.get_next_packet()
            si = hl2ss.unpack_si(data.payload)
            head_pose = si.get_head_pose()
            print("..............")
            print(head_pose.position)


            # head_position_string = struct.pack(f"!{len(head_pose.position)}f", *head_pose.position)
            head_position_string = f"{head_pose.position}".encode()
            conn.sendall(head_position_string)
            # Wait for a while before sending the next message
            time.sleep(1)

client.close()
listener.join()
