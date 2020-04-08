#Author:Anliu
#!/bin/bash/env python3.7
#Author:zhao
#购物车
budget = int(input("请输入您的预算:"))
shop_list = [
    [1, 'iphone11', 6799],
    [2, 'keyboard', 249],
    [3, 'coffee', 32],
    [4, 'pen', 80],
    [5, 'bicycle', 1500]
]
user_list = []
price = 0
balance = budget
exit_flag = False
print("商品列表如下:\n"+"-"*20+"\n编号 名称 价格")
for i in shop_list:
    for j in i:
        print(j, end=" ")
    print("")
print("-"*20)
while not exit_flag:
    select = input("请选择需要购买的商品编号(退出Q/q)：")
    if select == "q" or select == "Q":
        exit_flag = True
    else:
        select = int(select)
    while not exit_flag:
        if select > len(shop_list):
            print("商品编号不存在，请重新输入！")
            break
        else:
            number = shop_list[select-1][0]
            product = shop_list[select-1][1]
            price = int(shop_list[select-1][2])
        if budget >= price:
            user_list.append(product)
            balance = balance - price
            print("扣款{0}元，当前余额{1}元".format(price, balance))
        elif balance < price:
            print("您的余额不足，无法购买该商品！")
        break
if balance == budget:
    print("您本次未消费，余额为{0}元".format(budget))
else:
    print("已购买商品:", end=" ")
    for j in user_list:
        print(j, end=" ")
    print("\n本次您共消费{0}元,余额为{1}元,欢迎下次再来!".format(price, budget))