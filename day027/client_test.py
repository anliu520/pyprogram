#Author:Anliu
import socket
c = socket.socket()
c.connect(("127.0.0.1",9898))
#c.connect_ex(("127.0.0.2",9898))
while True:
    mgs = input(">>>:")
    r = c.send(mgs.encode("utf-8"))
    data  = c.recv(1024)
    print(r)
    print(data)
    print(c.getpeername())
    print(c.getsockname())
    print(c.fileno())

c.close()