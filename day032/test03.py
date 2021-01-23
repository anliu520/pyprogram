#Author:Anliu
#Author:Anliu
import threading,time
#event = threading.Event()

def lighter():
#    event.set()
    count = 0
    while True:
        if  count >5 and count <=10:
#            event.clear()  #把标志位清空
            #print("\033[41;1 红灯亮... \033[0m")
            print("\033[41;1m--red light on---\033[0m")

        elif count >10:
#            event.set()  #设置标志位
            count = 0

        else:
            #print("\033[42;1 绿灯亮... \033[0m")
            print("\033[42;1m--green light on---\033[0m")

        time.sleep(1)
        count += 1

def car(name):
    while True:
        if event.is_set(): #判断是否置位
            print("[%s] running ..." %name)
            time.sleep(1)
        else:
            print("[%s] wainting ..."%name)
            event.wait()
            print("\033[34;1m [%s] start gonging ..."%name)


t = threading.Thread(target=lighter,)
t.start()
c = threading.Thread(target=car,args=("tuolaji",))
c.start()