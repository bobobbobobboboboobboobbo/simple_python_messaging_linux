import socket

HOST = input('Host Server: ')  # The server's hostname or IP address
PORT = 65432      # The port used by the server
import socket

HOST = input("host IP Adress: ")  # The server's hostname or IP address
PORT = 65432        # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        # Send message to server
        message = input("Enter message to send to server: ")
        s.sendall(message.encode('utf-8'))

        # Receive message from server
        data = s.recv(1024)
        if not data:
            break
        print('____________________________\n'f"Received from server: {data.decode('utf-8')}")
