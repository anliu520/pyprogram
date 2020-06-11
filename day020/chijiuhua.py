#Author:Anliu
import json,pickle,shelve
dict = {"":""}
list = ["",""]
name = "anliu"

def run():
    print("this is a fun ....")

class RUN():
    def bar(self):
        print("this is a obj....")

with open("test","w") as f1:
    json.dump(dict,f1)
    json.dump(list,f1)
    json.dump(name,f1)
#    json.dump(run,f1)
#    json.dump(RUN,f1)
'''
with open("test","r") as f2:
    print(json.load(f2))
'''


#a = json.dumps(dict)   #把字典等数据类型持久化为字符串类型。
#                       # 字典  -----> 二进制
#                       # dict  --dunmps（）-->字符串 ---.encode()--->二进制  --->socket
#print(a.encode(),type(a))
#
#b = json.loads(a)
#print(b,type(b))
#
#a = pickle.dumps(dict)
#print(a,type(a))
#b = pickle.dumps(list)
#print(b,type(b))
#c = pickle.dumps(name)
#print(c,type(c))
#d = pickle.dumps(run)
#print(d,type(d))
#e = pickle.dumps(RUN)
#print(e,type(e))
####socket()---->  :
#d1 = pickle.loads(d)
#print(d1,type(d1))
#d1()
#
#e1 = pickle.loads(e)
#print(e1,type(e1))
#m = e1()
#m.bar()
#

d1 = shelve.open("file")
#d1["dict"] = dict
#d1["list"] = list
#d1["name"] = name
d1["fun"] = run
a = d1.get("dict")
print(a,type(a))
b = d1.get("name")
print(b,type(b))
c = d1.get("list")
print(c,type(c))
d = d1.get("fun")
print(d,type(d))
d()






