#Author:Anliu
import json
import random
from core import db_handle
from conf import setting
#ccount =
db_path = db_handle.db_handle(setting.DATABASE)
#print(db_path)
#account_file = "%s" %(db_path)
def account_input(username,password):
    """
    函数功能是账号输入的总接口
    :param username: 用户名
    :param password: 用户密码
    :return: 以元组的形式返回两个值，一个是用户，另一个是密码
    """
    username = input("请输入账号：")
    password = input("请输入密码：")
    return username,password

def account_register():
    """
    函数功能是账号注册
    :return: 如果账号注册成功，则返回0，账号注册失败返回1
    """
    a = account_input("user", "pass")
    _username = a[0]
    _password = a[1]

    with open(db_path,"r") as f0:
        account = json.load(f0)

    account.update({_username:_password})
    with open(db_path,"w") as f1:
        json.dump(account,f1)
    return 0
#account_register()

def account_frozen(username):
    '''
    该函数功能是当账号或密码输入错误时，锁定账号
    :param username: 传递需要锁定的账号
    :return:
    '''
    ran_pass = random.randrange(100000, 1000000)
    with open(db_path,"r") as f1:
        account = json.load(f1)
        account[username] = ran_pass
        with open(db_path, "w") as f2:
            json.dump(account, f2)

def account_loggin():
    '''
    该函数功能是实现账号验证
    :return:
    '''
    count = 0
    while count < 3:
        count += 1
        with open(db_path,"r") as f2:
            account_dict = json.load(f2)
            a = account_input("user", "pass")
            username = a[0]
            password = a[1]

            # 判断输入账号是否与注册信息匹配。
            if username not in account_dict.keys():
                print("账号未注册，请注册后登录")
                exit()
            elif username in account_dict.keys() and password == account_dict.get(username):
                print("登录成功...")
                return username,account_dict[username]
            else:
                print("账号密码不正确，请重新输入...")
    #循环正常退出，则账号锁定。
    else:
        account_frozen(username)
        print("账号已经锁定，请联系管理员开通...")
        exit()
#account_loggin()
