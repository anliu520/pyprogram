#Author:Anliu
#Author:Anliu
from multiprocessing import Process,Queue
import threading,queue
#def f(q):
def f(q):
    q.put([42, None, 'hello'])

if __name__ == '__main__':
    q = Queue()
    p = Process(target=f, args=(q,))
    #p = threading.Thread(target=f,)
    p.start()
    print(q.get())  # prints "[42, None, 'hello']"
    p.join()
