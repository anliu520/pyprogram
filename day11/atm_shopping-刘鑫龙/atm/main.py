#Author:Anliu

import os,sys
base_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(base_dir)
from core import main
from core import manage
from core import super_manage
def main2():
    while True:
        print("欢迎进入ATM界面")
        print("\t1.用户")
        print("\t2.管理员")
        print("\t3.超级管理员")
        choise = input("选择进入(q退出程序)>>:").strip()
        if choise == "1":
            main.run()
        elif choise == "2":
            manage.run()
        elif choise == "3":
            super_manage.run()
        elif choise == "q":
            exit(0)