#Author:Anliu
import queue,threading
list1 = queue.Queue()  #先进先出
list2 = queue.LifoQueue(maxsize=5)   #先进后出
def listput():
    for i in range(5):
        #print(i)
        list2.put(i,block=True,timeout=None)
        #if queue.Full:
        #    print("撑死了...")
listput()
#print("len is :",list2.qsize())
#print(list2.get())
#print(list2.get())
#print(list2.get())
#print(list2.get())
#if queue.Empty():
#    print("到头了...")

#print(list2.get(block=True,timeout=None))
#list2.get_nowait()




def listget():
    for i in range(6):
        print(list2.get())
        print(list2.task_done())
        list2.get_nowait()
listget()

#p = threading.Thread(target=listput,args=())
#g = threading.Thread(target=listget,args=())
#p.start()
#g.start()