#Author:Anliu
import socket
c = socket.socket()
#c.connect(("127.0.0.1",9999))
c.connect(("192.168.42.3",9999))

while True:
    cmd = input(">>>:")
    if len(cmd) == 0:continue
    c.send(cmd.encode())
    data = c.recv(1024)
    print(data.decode())
