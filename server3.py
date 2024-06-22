import socket

def server_program():
    host = '0.0.0.0'
    port = 5006

    server_socket = socket.socket()
    server_socket.bind((host, port))
    server_socket.listen(2)
    print("Server is listening on port", port)

    conn, address = server_socket.accept()
    print("Connection from:", address)

    while True:
        data = conn.recv(1024).decode()
        if not data:
            break
        print("from connected user:", data)
        data = input(' -> ')
        conn.send(data.encode())

    conn.close()

if __name__ == '__main__':
    server_program()