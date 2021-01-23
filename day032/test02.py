#Author:Anliu
import time
import threading

redlight = False
def traffic_lights(n):
    count = 0
    global redlight
    while True:
        if count > 5 and count <10 :
            print("红灯亮...")
            redlight = True
        elif count > 10:
            count = 0
            #global redlight
            redlight = False
        else:
            print("绿灯亮...")
        count += 1
        time.sleep(2)

def car(n):
    while True:
        time.sleep(2)
        if not redlight:
            print("car is running ...")
        else:
            print("car is waiting...")


t = threading.Thread(target=traffic_lights,args=(0,))
c = threading.Thread(target=car,args=(0,))

t.start()
c.start()