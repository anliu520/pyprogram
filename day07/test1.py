#Author:Anliu

def test(*args):   #传递参数组，只能传递位置参数
    print(args)    #输出的结果就是一个元组
    print(args[0])  #使用元组的方法

#test("zhangkai","18")  # 位置参数
#test("dongyu","22","linux","120")
#test(['1','2','linux'],'yaobin','111','')


def test1(**kwargs):  #传递关键字参数，把关键字转化字典
    print(kwargs)
    print(kwargs["name"])  #调运字典的方法

#test1(name = "anliu",age="18")


def test3(*args,**kwargs):  #可以传递位置参数，也可以传递位置参数
    print(args)
    print(kwargs)

#test3("1",n="name")

def test4(name,age=18,**kwargs):   #在形式参数上设置默认值
    print(name)
    print(age)
    print(kwargs)
#test4("anliu",a=20)

def test5(name,*args):
    print(name)
    print(args)

test5("123",["1","2","3"],"123","anliu")






