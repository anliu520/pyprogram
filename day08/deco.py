#Author:Anliu
import time

def deco_time(fun):       #fun将接受的是被装饰函数的内存地址对象
    def in_deco(*args,**kwargs):
        print(time.strftime("%Y-%m-%d %X"), end=" ")
        fun(*args,**kwargs)   # test2(),真正运行被装饰函数  args:(1,2,3);*args:1,2,3  kwargs:({});**kwargs:
        #print(time.strftime("%Y-%m-%d %X"), end=" ")

    return in_deco     #返回的是嵌套函数的内存地址对象
#test2 = deco_time(test2)   #test2 = 嵌套函数的内存地址对象
#test2()                    #in_deco()

@deco_time   #test2 = deco_time(test2)  #语法糖
def test1():
    print("test1")
    pass
test1()


@deco_time
def test2(a,b,c):
    print("test2:",a+b+c)
    pass

test2(1,2,3)  #in_deco()


@deco_time
def test3():
    print("in the test3")
test3()