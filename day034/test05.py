#Author:Anliu
import gevent
def func1():
    print("\033[31;1m  事件1 \033[0m")
    gevent.sleep(3)
    print("\033[31;1m  事件2 \033[0m")

def func2():
    print("\033[31;1m  事件3 \033[0m")
    gevent.sleep(1)
    print("\033[31;1m  事件4 \033[0m")

def func3():
    print("\033[31;1m  事件5 \033[0m")
    gevent.sleep(0)
    print("\033[31;1m  事件6 \033[0m")

gevent.joinall([
    gevent.spawn(func1),
    gevent.spawn(func2),
    gevent.spawn(func3),
])

