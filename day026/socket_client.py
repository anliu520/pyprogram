#Author:Anliu
import socket,json
client = socket.socket()                 #生成一个socket实例
client.connect(("localhost",9999))      #链接服务端
#client.connect(("192.168.42.3",9999))

dict = {"ip":None}

while True:
    cmd = input(">>>:").strip()         #输入
    dict["ip"] = cmd
    if len(cmd) == 0 :continue          #判断输入是否为空
    #client.send(cmd.encode("utf-8"))    #发送数据
    ip = json.dumps(dict)
    client.send(ip.encode())
    mge = client.recv(1024)              #接受数据
    f1 = open("mysql","bw")
    f1.write(mge)
    print(mge)
