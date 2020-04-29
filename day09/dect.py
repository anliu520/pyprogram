#Author:Anliu


#装饰器本质就是函数。

def logger(func):  #被装饰函数的内存地址对象
    def timer(*args,**kwargs):
        print("logger:")
        func(*args,**kwargs)    #test1()
        print("------------")

        #vars()
        #test1()
        #rint("This is a test")
    return timer  #嵌套函数的内存地址对象

@logger    ##test1 = logger(test1)  #嵌套函数内存地址对象,（语法糖）

def test1(name):   #函数即变量， test1 = ""
    print("This is a test of %s"%name)

test1("lisi")

@logger
def test2():
    print("This is a test ")

test2()