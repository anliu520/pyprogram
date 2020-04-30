#Author:Anliu

from collections import Iterable
from collections import Iterator

list = ["linux","mysql","nginx","","...","memcached"]
tuple = ()
str = ""
dict = {}

list_i = iter(list)
print(isinstance(list,Iterator))
print(isinstance(list_i,Iterator))
#print(list.)
print(list_i.__next__())
print(list_i.__next__())
print(list_i.__next__())


#print(isinstance(list,Iterable))
#print(isinstance(tuple,Iterable))
#print(isinstance(tuple,Iterable))
def fib(max):
    n,a,b = 0,0,1
    while n < max:
        yield b     #保存了函数的中断状态，并返回
        a,b = b,a+b
        n = n+1
    return "down"
#f = fib(8)


#print(isinstance(f,Iterator))


#print(isinstance(f,Iterable))
#
#list2 = (i*2  for i in range(10000000000000000))  #生成器
#print(list2)

#list2.__next__()
#print(isinstance(list2,Iterator))

#print(isinstance(list2,Iterable))


with open("test","r",encoding="utf-8") as f:
    for i in f:   #for ===》迭代器
        print(i.strip())
