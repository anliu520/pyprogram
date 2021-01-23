#Author:Anliu\

from multiprocessing import Process, Manager

def f(d, l):
    d[1] = '1'
    d['2'] = 2
    d[0.25] = None
    l.append(1)
    #print(l)

if __name__ == '__main__':
    with Manager() as manager:   #生成一个manager对象manager
        d = manager.dict()        #定义一个字典可以在多个进程间共享传递
        l = manager.list(range(5))  #定义一个列表可在多个进程间共享传递
        p_list = []
        for i in range(10):
            p = Process(target=f, args=(d, l))
            p.start()
            p_list.append(p)
        for res in p_list:
            res.join()

        print(d)
        print(l)

