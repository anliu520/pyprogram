#Author:Anliu
class People:
    '''
    This is a People class....
    '''
    #num = "anliu"
    def __init__(self,name,age):
        self.name =name
        self.age = age  #实例方法

    def eatting(self):
        '''
        eatting
        :return:
        '''
        print("eating....")

    def sleep(self):
        print("sleep ...")

    def talk(self):
        print("tslk....")

    def __call__(self, *args, **kwargs):
        print(*args,**kwargs)
        return 123

    def __str__(self):
        return "dadada"

    def __getitem__(self, item):
        print('__getitem__',item)

    def __setitem__(self, key, value):
        print("__setitem__",key,value)

    def __delitem__(self, key):
        pass

def running():
    print("running...")

num = "longlong"

#print(People("zhangsan","28")())
p1 = People("lisi","29")
p2 = People("zhangsna","28")

#'''
#判断类中有没有方法running，若有running方法直接执行，若没有，将类外部的
#函数添加到类中。
#'''
#if hasattr(People,"running"):    #判断类种有没有running字段
#    p1.running()
#else:
#    setattr(p1,"running",running)    #将外部的running函数添加到类中
#    p1.running()
#
#    #print(hasattr(People,"num"))
'''
判断类中有没有变量num，若有num直接调运，若没有，将类外部的
num变量添加到类中。
'''
if hasattr(People,"num"):
    print(p1.num)
else:
    setattr(p1,"num",num)
    print(p1.num)
    #delattr(p1,num)   #删除变量
    print(p1.num)


fun = getattr(p1,"talk")
fun()
#
#
#print(hasattr(People,"talk"))
#
#if hasattr(People,"talk"):
#    fun = getattr(People,"talk")
#    fun("123")
#    p1.talk()
#
#else:
#    print("方法不存在...")




#p2["k1"] = "anliu"
#p2["k1"]

#print(p1,p2)
#p.eatting()

#print(People.__dict__)
#print(People.__dict__)

#p("liming",["na","29"])
#print(p())
#p.eatting()

#print(p.__doc__)
#p.eatting()
#

