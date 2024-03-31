import socket

HOST = ''  # Leave blank for all interfaces
PORT = 65432  # Port remains the same

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            if not data:
                break
            print(f"Received message: {data.decode('utf-8')}")  # Decode and print
            conn.sendall(data)