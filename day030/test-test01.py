#Author:Anliu

import threading
import time

def run(n):
    print("task",n)
    time.sleep(2)

for i in range(100):
    ti = threading.Thread(target=run,args=("aaaaa",))
    #t2 = threading.Thread(target=run,args=("aaaaa",))
    ti.start()
    #t2.start()