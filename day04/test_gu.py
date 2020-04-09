#Author:Anliu
username = ["tom","jerry","dancy","bob"]
passwd = ["123","456","789","abc"]
product = [
    ("phone1",1000),
    ("phone2",2000),
    ("phone3",3000),
    ("phone4",4000),
    ("phone5",5000)
]
num = 0
cart = []
money = []
user_lock = []
exit_flag = False
while not exit_flag:
    name = input("请输入您的用户名：")
    password = input("请输入您的密码：")
    if name in username and password == passwd[username.index(name)]:
        print("欢迎您登录！")
        if name in money:
            money1 = money[money.index(name)][1]
        else:
            money1 = int(input("请输入您的预算："))
            money.extend([name,money1])
            print(money)
        # print(money[money.index(name)][1])
        while not exit_flag:
            for i in product:
                print(product.index(i)+1,i)
            choice2 = input("请选择您想购买的商品编号(退出请按q，返回请按b)：")
            if choice2.isdigit():
                choice2 = int(choice2)
                if choice2 >0 and choice2 <len(product)+1:
                    #print(product[choice2-1][1],type(product[choice2-1][1]))
                    if money1 >= product[choice2-1][1]:
                        cart.append(product[choice2-1][0])
                        money1 = money1 - product[choice2-1][1]
                        print(money[money.index(name)])
                        money[money.index(name)+1] = money1
                        print("您购买了：%s. 余额：%s"%(cart,money[money.index(name)][1]))
                    else:
                        print("您的余额不足:%s，请选择其他商品！"%money1)
            elif choice2 == "q":
                 exit_flag = True
            elif choice2 == "b":
                break
    # elif name in

    elif name not in username:
       choice1 = input("没有此用户，是否注册（y|n）：")
       if choice1 == "y":
           while not exit_flag:
                name1 = input("请输入您需要注册的用户名：")
                passwd1 = input("请输入您的密码：")
                passwd2 = input("请再次确认您的密码：")
                if passwd1 == passwd2:
                    username.extend([name1])
                    passwd.extend([passwd1])
                    print(username,passwd)
                    break
                else:
                    pass