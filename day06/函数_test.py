#Author:Anliu
import time
def time_test():
    '''
    该函数是用来打印系统时间。
    :return: 默认是0，若果是0则表示...，
    '''

    if 1:
        flag = 1
    else:
        flag = 0
    time_format = "%Y-%m-%d %X"
    time_current = time.strftime(time_format)
    print(time_current,end=" is log ")
    return flag

def test1():
    time_test()
    print("test1")
    #return {"L1921":["tianhao","runrun","yaobin"],"L1931":["","",""]}
    #return ("10000","112e","dsf")
    #return "linux","java","php",["123","qrw","111"],{"L1921": \
    # ["tianhao","runrun","yaobin"],"L1931":["","",""]}
    #return time_test()
    return time_test

def test2(x,y,z):  #形式参数
    '''
    函数是用来搞笑的
    :param x: 1
    :param y: 2
    :return: x+y
    '''

    time_test()
#    print(x+y)
    return x+y+z

def test3():
    time_test()
    print("test3")

#print(time_test())
#print(test1()())
#test1()

#a = test2(y=1,x=2)  #实参
a = test2(1,y=2,z=3)  #实参
print(a)
#test3()