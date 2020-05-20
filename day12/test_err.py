#Author:Anliu
import json
try:
    with open("file1","r",encoding="utf-8") as f:
       tmp = json.loads(f)

except FileNotFoundError:
    print("报错了..")

else:
    print("我代表一万行代码。。。")

try:
    a=1/0  #
    print(a)
except ZeroDivisionError :
    print("又来了一万行代码....")

else:
    print("....")
