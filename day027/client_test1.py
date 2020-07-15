#Author:Anliu
import socket,time
client = socket.socket()
#client.connect(("127.0.0.1",8888))
client.connect(("192.168.42.3",8888))
while True:
    mgs = input(">>>:").strip()
    if len(mgs) == 0: continue
    client.send(mgs.encode("utf-8"))
    data = client.recv(1024)
    client.send(b"ack")
    #print(data.decode("utf-8"))
    cmd_size = 0
    received_data = b""
    while cmd_size < int(data.decode("utf-8")):
        cmd_data = client.recv(1024)
        cmd_size += len(cmd_data)
        received_data += cmd_data
    else:
        print(received_data.decode())
