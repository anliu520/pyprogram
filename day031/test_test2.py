#Author:Anliu

#Author:Anliu
import threading
import time

def run(n):
    global num
    #time.sleep(0.8)
    num +=1  #0+1+1+1+1..1000

num = 0
t_objs = []
for i in range(1000):  #==0
    t = threading.Thread(target=run,args=("t-%s"%i,))
    t.start()
    t_objs.append(t)

for t in t_objs:
    t.join()

print("-------------all threads has finished...",threading.current_thread(),threading.active_count())
print("num",num)
