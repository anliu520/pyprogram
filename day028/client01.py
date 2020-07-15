#Author:Anliu
import socket
def fun_client():
    c = socket.socket()
    #c.connect(("127.0.0.1",9999))
    c.connect(("127.0.0.1",9898))

    while True:
        #cmd = input(">>>:")
        cmd = "this is a test"
        c.send(cmd.encode())
        mgs = c.recv(1024)
        print(mgs)

for i in range(10):
    fun_client()