#Author:Anliu
import socket
server = socket.socket()       #生成一个socket对象
server.bind(('localhost',9999))   #绑定IP和端口

server.listen()                    #进入监听状态
print("正在等数据...")
while True:
    conn,addr = server.accept()        #接受客户端实例和地址conn: 实例，addr：客户端的地址和端口
    try:
        while True:
            data = conn.recv(1024)             #接受数据
            conn.send(data.upper())
            print(data)                        #打印数据
    except ConnectionResetError as key:
        pass
