#Author:Anliu
from multiprocessing import Process,Pool
import time
def Foo(n):
    time.sleep(2)
    print("This is a For")
    return n + 100
def bar(rag):
    print("this is a back valuse : ",rag)   #回调函数接受的参数将是调运函数的返回值。
if __name__ == '__main__':
    pool = Pool(2)
    for n in range(10):
        #pool.apply(func=Foo,args=(n,))  #同步
        pool.apply_async(func=Foo,args=(n,),callback=bar)   #异步，回调函数是bar
    #pool.join()
    pool.close()
    pool.join()  #进程池中进程执行完毕后再关闭，如果注释，那么程序直接关闭。
