#Author:Anliu
#Author:Anliu
import time
import threading

event = threading.Event()

def traffic_lights(n):
    count = 0
    event.set()
    while True:
        if count > 5 and count <10 :
            print("红灯亮...")
            event.clear()
        elif count > 10:
            count = 0
            #global redlight
            event.wait()
        else:
            print("绿灯亮...")
        count += 1
        time.sleep(2)

def car(n):
    while True:
        time.sleep(2)
        if event.is_set():
            print("car is running ...")
        else:
            print("car is waiting...")


t = threading.Thread(target=traffic_lights,args=(0,))
c = threading.Thread(target=car,args=(0,))

t.start()
c.start()