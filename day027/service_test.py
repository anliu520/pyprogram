#Author:Anliu

import socket
s = socket.socket(family=socket.AF_INET,type=socket.SOCK_STREAM)
s.bind(("127.0.0.1",9898))
s.listen()
print("等待数据...")
s.settimeout(20)
print(s.gettimeout())
conn,addr = s.accept()
print(addr)
while True:
    try:
        #conn.setblocking(0)
        data = conn.recv(10)
        if len(data) == 0: break
        print(type(data))
        conn.send(data.upper())
        #conn.sendall(data.upper())
        print(conn.getpeername())
        print(conn.getsockname())
        #conn.setsockopt()
        #print(conn.getsockopt())
        f1 = conn.makefile()
        print(f1)

    except ConnectionResetError as key1:
        pass
conn.close()

