import socket

HOST = ''  # Leave blank for all interfaces
PORT = 65432  # Port remains the same
import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            # Receive message from client
            data = conn.recv(1024)
            if not data:
                break
            print('______________________\n' f"Received from client: {data.decode('utf-8')}")

            # Send message to client
            message = input("Enter message to send to client: ")
            conn.sendall(message.encode('utf-8'))
