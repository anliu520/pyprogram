#Author:Anliu
def test1(a,b):
    c = a+b
    print("ninhao")
    return c
    print("ninhao")

a = test1(1,2)
print(a)

def test2(a,b):
    c = a+b
    print(c)

#print(test2(test1(2,4),4))  #a=6

def bar():
    print("in the bar")
    #return "hehe"

def test(fun):
    fun()   #print(bar())

#test(bar)

def foo():
    print("the foo")
    def bar():
        print("The bar")
    bar()

#foo()

cal = lambda x:x*3

cal2 =(lambda x,y:x*y)

#print(cal2(3,5))

#print(cal(3))




