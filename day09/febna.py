#Author:Anliu
'''
a,b = 0,1
for i in range(20):
    a,b = b,a+b
    print(b)
'''

def fib(max):
    n,a,b = 0,0,1
    while n < max:
        yield b     #保存了函数的中断状态，并返回
        a,b = b,a+b
        n = n+1
    return "down"
f = fib(8)  # 36s   ---->   等待;

print(f.__next__())
#函数状态已中断，1
print("开学啦，")
print(f.__next__())
print("我们好开心，，")
print(f.__next__())
print(f.__next__())
print(f.__next__())



#for i in range(15):
#    try:
#        print(f.__next__())
#    except StopIteration as e:
#        print("StopIteration:",e.value)
#


