#Author:Anliu
#Author:Anliu

import time

def timmer(func):
    def warpper(*args,**kwargs):
        start_time=time.time()
        func()
        stop_time=time.time()
        print("the func run time is %s"%(stop_time-start_time))
    return warpper

@timmer
def test1():
    time.sleep(3)
    print("in the test1")
test1()

@timmer
def test2():
    print("in the test2")
test2()