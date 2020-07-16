#Author:Anliu
import socketserver
socketserver.time()
class MyTcpHandle(socketserver.BaseRequestHandler):
    '''
    定义了一个请求类
    '''
    def handle(self):
        try:
            while True:
                #conn,addr = self.server.accept()
                self.data = self.request.recv(1024)
                print(self.data)
                print("-----------一次请求：结束了----------")
                self.request.send(self.data)
        except ConnectionResetError as key:
            pass

if __name__ == '__main__':
    #server = socketserver.TCPServer(("127.0.0.1",9999),MyTcpHandle)
    server =socketserver.ThreadingTCPServer(("127.0.0.1",9999),MyTcpHandle)
    #server.handle_request()
    server.serve_forever()
    server.server_close()