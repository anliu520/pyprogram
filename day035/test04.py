#Author:Anliu
import socket
import threading
def sock_conn():
    client = socket.socket()
    client.connect(("localhost",8001))
    count = 0
    while True:
        client.send( ("hello %s" %count).encode("utf-8"))
        data = client.recv(1024)
        print("[%s]recv from server:" % threading.get_ident(),data.decode()) #结果
        count +=1
    client.close()
for i in range(1000):
    t = threading.Thread(target=sock_conn)
    t.start()