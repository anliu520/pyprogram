#Author:Anliu
import socket
s = socket.socket()
s.bind(("127.0.0.1",9999))
s.listen()
while True:
    conn,addr = s.accept()

    try:
        while True:
            data = conn.recv(1024)
            print(type(data))
            conn.send(data.upper())
    except ConnectionResetError as key:
        pass