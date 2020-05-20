#Author:Anliu
import random
l = ["linux","nginx","php","mysql"]

print(int(random.random()*100000))
print(random.randint(10000,99999))
print(random.choice(["zhangkai","jiakai","liming"]))  #字符串，列表，元组
print(random.sample("hello",4))
print(l)
random.shuffle(l)
print(l)