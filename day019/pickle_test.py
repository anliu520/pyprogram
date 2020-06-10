#Author:Anliu
import pickle,json
dict = {"hostname":"zabbix",
        "IP":"192.168.42.111"
        }

pic = pickle.dumps(dict)
print(type(pic))
conver = pickle.loads(pic)
print(conver)

def logging():
    print("tihis is a longgging ....")

m = pickle.dumps(logging)
print(m,type(m))

n = pickle.loads(m)
print(n,type(n))
n()

