#Author:Anliu
'''
list = []
for i in range(10000):
    print(i)
    list.append(i)

print(list)

for n in list:  #10000  == 内存 10000 --- 10
    if list.index(n) < 10:
        print(n*2)

'''
list1 = [ i*2  for i in range(10)]   #列表生成式
print(list1)
list2 = (i*2  for i in range(10000000000000000))  #生成器
print(list2)

#for n in range(10):
#    print(list2.__next__())   #生成器开始生效


for n in range(5):
    list2.__next__()
#print(list2.__next__())
#print(list2.__next__())

