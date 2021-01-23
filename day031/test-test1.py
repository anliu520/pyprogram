#Author:Anliu
import threading
import time,os
class Mytest(threading.Thread):
    def __init__(self,n):
        super(Mytest,self).__init__()
        self.n = n
    def run(self):
        print("This is a %s"%self.n , "Threa:" ,threading.current_thread().ident,"PID:",os.getpid(),os.getppid())
        time.sleep(2)

for i in range(50):
    t = Mytest(i)
    t.setDaemon(True)   #thread id ---->PID   :当主线程结束后，守护线程必将结束，所以看不到2s的阻塞
    t.start()

#print(os.getpid())
#t2 = Mytest("2")
#t2.start()
