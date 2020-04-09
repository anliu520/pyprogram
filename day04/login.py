#Author:Anliu
import json
import random
#_username = "anliu"  #保存在了内存  === 持久化（硬盘）（File，mysql,redis（持久化））
#_password = "123"
# 写入文件 ---> 打开 ---> 写 ----> 关闭
#序列化：  内存对象---->硬盘
#反序列化： 硬盘----->内存对象
# 开发---（log）--- File

#info = {"anliu":"123","zhangsan":"123","lisi":"123"}
#with open("account","w") as f:
#    json.dump(info,f)

mun = 0
while mun <3:
    username = input("username:")
    password = input("password:")
    #print(info.keys())
    with open("account","r") as f:
        info = json.load(f)
       #print(info)
    if username not in info.keys():
        print("账户不存在，请注册...")
        exit()
    elif info.get(username) == password:
        print("欢迎登录...")
        exit()
    else:
        print("用户密码错误，请重新输入...")
    mun +=1
else:
    ran_pass = random.randrange(100000,1000000)
    info = {"anliu": "123", "zhangsan": "123", "lisi": "123"}
    info[username] = ran_pass
    with open("account", "w") as f:
        json.dump(info, f)
    print("账号已经冻结，请联系管理员开通...")  #重置随机密码

