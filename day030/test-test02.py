#Author:Anliu
import threading
import time
class MyThread(threading.Thread):
    def __init__(self,n):
        super(MyThread,self).__init__()
        self.n = n

    def run(self):
        print("running task:",self.n,threading.current_thread())
        time.sleep(2)

before_time = time.time()
tmp = []
for i in range(50):
    t = MyThread("123456")
    tmp.append(t)
    t.start()

#print(threading.current_thread())
print(threading.active_count())

for k in tmp:
    k.join()


print("经历时间：" ,time.time()-before_time)