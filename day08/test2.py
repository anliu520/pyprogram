#Author:Anliu

#递归：

def recurcsion(n):
    if int(n/2) > 0:
        return recurcsion(int(n/2))
    print(">>>",n)
#recurcsion(10)

def test1(a,b):
    c = a+b
    return c

def test2(a,b):
    c = a+b
    print(c)

b = test2(test1(2,4),4)  #a=6
print(b)

#test2(test1(1,2),3)  #test1(1,2)==>3,test2(3,3)

def bar():
    print("in the bar")

def test(fun):
    print(fun())
#test(bar)


#print(bar)



#def test1():
#    print("test1")

#def test2():
#    print("test2")
#    test2()

#test2()


