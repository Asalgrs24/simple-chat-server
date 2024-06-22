import socket

def client_program():
    host = '172.17.0.2'
    port = 5006

    client_socket = socket.socket()
    client_socket.connect((host, port))
    print("Connected to server")
    message = input(" -> ")

    while message.lower().strip() != 'bye':
        client_socket.send(message.encode())
        data = client_socket.recv(1024).decode()
        print('Received from server:', data)
        message = input(" -> ")

    client_socket.close()

if __name__ == '__main__':
    client_program()