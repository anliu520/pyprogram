#Author:Anliu

import queue,random,time
import threading

list = queue.Queue()
def Product():
    while True:
        print("开始造数据了....")
        list.put(random.randrange(5))
        time.sleep(1)
def Concumer():
    while True:
        time.sleep(2)
        if not list.empty():
            print("获取到的值为：",list.get())
        else:
            print("没数据了...取了毛线...")
P = threading.Thread(target=Product,args=())
C1 = threading.Thread(target=Concumer,args=())
C2 = threading.Thread(target=Concumer,args=())
C3 = threading.Thread(target=Concumer,args=())
P.start()
C1.start()
C2.start()
C3.start()