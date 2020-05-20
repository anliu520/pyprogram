#Author:Anliu
#捕捉SystemExit异常，可以做一些工作，如打印异常消息等：
#Author:Anliu
import sys

def f1(str):
    global sports
    if str.upper() == "EXIT":
        sys.exit("User exit")  # 触发异常SystemExit，退出 key：User exit
    else:
        sports.append(str)
        sys.exit()             # 触发异常SystemExit，退出 key：“”

user = ['zhangkai','jiakai','liming']
for usr in user:
    sports = []
    print(usr + ",input your favorite sport and type exit tp exit.")
    while True:
        response = input(":")
        try:
            f1(response)
        except SystemExit as key:
            print(key)
            print(usr + "'s favorite sports is " + ",".join(i.lower() for i in sports) + '.')
            break