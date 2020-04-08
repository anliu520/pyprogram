#Author:Anliu
productList =[
    ("商品1",5888),
    ("商品2",3888),
    ("商品3",10000),
    ("商品4",2888),
    ("商品5",6999)
]
cart = []
exit_flag = False
moeny = int(input("请输入预算:"))
while not exit_flag:
    #for i in productList:
    #    print(productList.index(i)+1,i)
    for index,item in enumerate(productList):
        print(index+1,item)
    num = input("请输入要购买的商品编号（按回车即购买，输入e退出）：")
    if num.isdigit():
        num = int(num)
        if num <= len(productList)+1 and num >0:
            if moeny >= productList[num-1][1]:
                cart.append(productList[num-1])
                moeny = moeny - productList[num-1][1]
                print("您购买了%s，余额%s" %(productList[num-1][0],moeny))
            else:
                print("余额不足.%s..请选择请他商品"%moeny)
    elif num == "e":
        exit_flag = True
    else:
        print("您输入的编号好像不对哦...")
else:
    #for i in cart:
    for index,item in enumerate(cart):
        print(index+1,item)
