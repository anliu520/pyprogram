#Author:Anliu
import socket
client = socket.socket()                   #生成一个socket对象
#client.connect(('localhost',9999))        #链接服务端
client.connect(('192.168.42.3',9999))

while True:
    mgs = input(":>>>")
    if len(mgs) == 0:continue
    client.send(mgs.encode("utf-8"))   #发送数据
    data = client.recv(102400)
    print(data.decode("utf-8"))
    continue