import socket

HOST = input('Host Server: ')  # The server's hostname or IP address
PORT = 65432        # The port used by the server

def sentence_to_binary_list(sentence):
    binary_list = []
    for char in sentence:
        ascii_code = ord(char)
        binary_list.append(bin(ascii_code))
    return binary_list

      
import socket

while True:
    message = input("Enter your message: ")
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(message.encode('utf-8'))  # Encode the message as UTF-8 bytes
        data = s.recv(1024)
        print('Received', repr(data.decode('utf-8')))  # Decode the received data

    