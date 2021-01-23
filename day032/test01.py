#Author:Anliu
import threading
import time

def running(n):
    semaphore.acquire()    #申请信号量实例
    print("It's running....%s"%n)
    time.sleep(2)
    semaphore.release()   #释放

if __name__ == '__main__':
    semaphore = threading.BoundedSemaphore(5)    #生成一个信号量的实例，一次运行5个线程
    for i in range(10):
        t = threading.Thread(target=running,args=(1,))
        t.start()

