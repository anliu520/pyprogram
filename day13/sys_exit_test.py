#Author:Anliu
#Author:Anliu
import sys
#（1）sys.argv
#print(sys.argv)  #打印文件名以及参数
#a = sys.argv[0]  #传递位置参数
#b = sys.argv[1]
#print(a,b)

#（2）sys.exit(1)  退出程序机制
#通过引发SystemExit异常来退出Python程序。
#可以通过捕捉SystemExit异常，在finally语句中进行一些清理操作；不捕捉SystemExit异常（SystemExit异常不被认为是错误的异常）将直接退出程序。
#退出程序，正常退出为sys.exit(0)

#不捕捉SystemExit异常，直接退出程序：
#Author:Anliu
import sys,time

print("Type exit to exit.")
while True:
    response = input(">>>")
    if response.upper() == "EXIT":
        print("you have typed exit ,and system will exit right now...")
        time.sleep(0.1)
        sys.exit()
    print("you typed" + response + '.')

'''
#捕捉SystemExit异常，可以做一些工作，如打印异常消息等：
#Author:Anliu
import sys

def f1(str):
    global sports
    if str.upper() == "EXIT":
        sys.exit("User exit")
    else:
        sports.append(str)
        sys.exit()

user = ['zhangkai','jiakai','liming']
for usr in user:
    sports = []
    print(usr + ",input your favorite sport and type exit tp exit.")
    while True:
        response = input(":")
        try:
            f1(response)
        except SystemExit as msg:
            print(msg)
            print(usr + "'s favorite sports is " + ",".join(i.lower() for i in sports) + '.')
            break
            
'''
