# #!/usr/bin/env python
# # -*- coding: utf-8 -*-
# # author aliex-hrg.json
#
import os,sys
BASE_DIR = os.path.dirname(__file__)
print(BASE_DIR)
sys.path.append(BASE_DIR)

from atm import main
from shopping import shop
def main1():
    while True:
        print("ATM + 购物车功能小程序")
        print("\t1.逛商场")
        print("\t2.ATM管理")
        choise = input("选择进入(q退出程序)>>:").strip()
        if choise == "1":
            shop.man_shop()
        elif choise == "2":
            main.main2()
        elif choise == "q":
            exit(0)

if __name__ == '__main__':
    main1()
