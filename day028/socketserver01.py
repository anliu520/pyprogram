#Author:Anliu
import socketserver
socketserver.time()
class MyHandle(socketserver.BaseRequestHandler):
    '''
    请求处理类
    '''
    def handle(self):
        while True:
            try:
                self.data = self.request.recv(1024).strip()
                print("This is a data from client01",type(self.data))
                print(self.client_address)
                self.request.send(self.data.upper())
            except ConnectionResetError as key:
                break

#print(__name__)
if __name__ == '__main__':   #将该脚本直接运行时执行以下程序，#print(__name__) == __main__
    # 将该脚本当做模块传递时，一下程序不执行 #print(__name__) ==  socketserver01
    #用途：用于手动测试的程序可以写到判断之后。
    addr = ("127.0.0.1",9898)
    #server = socketserver.TCPServer(addr,MyHandle)    #实例化server，传递两个值，地址，处理类
    server = socketserver.ThreadingTCPServer(addr,MyHandle)
    #server.handle_request()  #接受一个请求
    server.serve_forever()   #接受多个请求
    server.server_close()   #关闭套接字
