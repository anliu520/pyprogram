#Author:Anliu
from  multiprocessing import  Process,Lock

def ruuning(n,l):
    l.acquire()
    print("This is a test ...%s"%n)
    l.release()

if __name__ == '__main__':
    l = Lock()
    for n in range(10):
        P = Process(target=ruuning,args=(n,l))
        P.start()

