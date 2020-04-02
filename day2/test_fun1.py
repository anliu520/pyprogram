#Author:Anliu
def fun_test():
    print("fun_test")
    return 0

def fun_test1():
    print("fun_test1")

def fun_test2():
    print("fun_test2")
    return 123,"liming",["linux","python"],{"liming":"xiaocui"}

def fun_test3():
    print("fun_test3")
    return fun_test2

def fun_test4():
    print("fun_test4")
    return fun_test2()
print(fun_test())
print(fun_test1())
print(fun_test2())
print(fun_test3()())
print(fun_test4())