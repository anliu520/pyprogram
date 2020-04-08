#Author:Anliu
#d = {"name":"DNS","IP":"192.168.0.1","linux":{"1921":["runrun","tongtong"]}}
#d1 = d.copy()
#d2 = d.copy()
#d1["linux"]["1921"][0] = "xiaobiaoza"
#print(d1)
#print(d2)
d1 = {'one':1,'two':2}
print(d1)
#d1.update({'three':3,"four":4})  #传递字典
#d1.update({'one':3,"four":4})
#d1.update(three=3,four=4)      #传递关键字
#d1.update([("three",3),("four",4)])   #传递一个或多个元组的列表
#d1.update(zip(["three","four"],["3","4"]))  #传递zip函数
d1.update(one=3,four=4)
print(d1)


#zip()将可迭代对象作为参数，将对象中对应的元素打包成一个个元组，然后返回这些元组组成的对象
a = [1,2,3]
b = [4,5,6]
c = [7,8,9,10]
#zipper = zip(a,b)
zipper = zip(a,c)
print(zipper)
#print(tuple(zipper))
print(dict(zipper))