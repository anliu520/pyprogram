#Author:Anliu
import queue
Queue = queue.Queue(2)
try:
    for i in range(3):
        print("putting....")
        #Queue.put(i)
        Queue.put_nowait(i)
except queue.Full as keys:
    pass
try:
    for i in  range(4):
        #print(Queue.get())
        print("Queue of len is  : ",Queue.qsize())
        print(Queue.get_nowait())
except queue.Empty as keys:
    print("队列已空...")