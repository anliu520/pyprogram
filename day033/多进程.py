#Author:Anliu

import  multiprocessing
import threading
import time,os
def Thread_running():
    print(os.getppid())
    print(os.getpid())
    print("I'm is a threading...",threading.get_ident())


def Running(name):
    print("This is a test of %s"%name)
    time.sleep(1)
    t = threading.Thread(target=Thread_running,args=())
    t.start()

if __name__ == '__main__':
    for i in range(10):
        P = multiprocessing.Process(target=Running,args=("hahaha",))
        P.start()
        #P.join()