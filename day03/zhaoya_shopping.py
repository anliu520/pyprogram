#Author:Anliu
moeny = input("请输入预算:")
productList =[
    ["商品1",5888],
    ["商品2",3888],
    ["商品3",10000],
    ["商品4",2888],
    ["商品5",6999],
]
if moeny.isdigit():
    moeny = int(moeny)
    lists = '---------------商品列表----------------\n'
    for index,item in enumerate(productList):
        lists += "No.%d, %s, ￥%d" %(index,item[0],item[1]) + "\n"
    print(lists)
    cart = []
    num = input("请输入要购买的商品编号（按回车即购买，输入e退出）：")
    while num != 'e':
        if num.isdigit():
            if(int(num) < len(productList)):
                item = productList[int(num)]
                if moeny >= item[1]:
                    cart.append(item)
                    moeny -= item[1]
                    print("您已购买[" + item[0] + "]，价值[￥" + str(item[1]) + "]，您的余额：￥" + str(moeny))
                else:
                    print("余额不足...请选择请他商品")
            else:
                print("商品编号不存在")
        else:
            print("您输入的编号好像不对哦...")
        num = input("请输入要购买的商品编号（按回车即购买，输入 e退出）：")

    conclusion = "--------------购物车列表-------------\n"
    for index,item in enumerate(cart):
        conclusion += "No.%d, %s, ￥%d" %(index,item[0],item[1]) + "\n"
    conclusion += "余额: "+str(moeny)
    print(conclusion)

else:
    print("您输入的金额不对")