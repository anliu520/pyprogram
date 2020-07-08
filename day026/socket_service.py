#Author:Anliu
import socket,json
server = socket.socket()               #生成一个socket实例
server.bind(("localhost",9999))       #绑定监听的地址和端口
server.listen()                        #监听
while True:
    print("等待数据。。。")
    conn,addr = server.accept()        #获取客户端的链接实例和地址（ip，port）
    try:
        while True:
            data = conn.recv(1024)     #接受消息
            if len(data) == 0: break   #判断接受消息是否为空，当客户端链接断开时
            ip = json.loads(data)
            print(ip)
            print(ip["ip"])
            conn.send(data.upper())
    except ConnectionResetError as key:  #当客户端断开时，抓取异常，保证客户端端口而服务端链接正常。
        pass

