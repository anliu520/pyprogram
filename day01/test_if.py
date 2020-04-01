#Author:Anliu
#猜一猜
ages = 48
num = 0
while num <3 :
    gas = input("请输入你认为老吕的年龄>>>:")
    if not gas.isdigit():
        print("请输入数字!!")
        exit()
    gas = int(gas)
    if gas == ages:
        print("恭喜你猜中了")
        exit()
    elif gas > ages:
        print("猜大了,,,")
    else:
        print("猜小了")
        co
    num +=1
else:
    print("xxxxxxxxxxxxxxxx")

