#Author:Anliu
import os
from core import db_handler
from conf import settings
from core import logger
from core import accounts
import json
import time


def acc_auth(user_data,account,password):
    '''
    文件认证接口
    :param account: 需认证的账号
    :param password: 需认证的密码
    :return: 认证通过返回账号对象，认证不通过返回null
    '''

    db_path = db_handler.db_handler(user_data)
    account_file = "%s/%s.json" %(db_path,account)
    #print(account_file)
    if os.path.isfile(account_file):
        with open(account_file,'r') as f:
            account_data = json.load(f)
            if account_data['password'] == password:
                exp_time_stamp = time.mktime(time.strptime(account_data['expire_date'], "%Y-%m-%d"))
                if time.time() >exp_time_stamp:
                    print("\033[31;1mAccount [%s] has expired,please contact the back to get a new card!\033[0m" % account)
                else: #passed the authentication
                    return  account_data
            else:
                print("\033[31;1mAccount ID or password is incorrect!\033[0m")
    else:
        while True:
            account_bar = input("\033[31;1mAccount [%s] 账户不存在是否立即注册！（y,n）\033[0m" % account)
            if account_bar == "y":
                accounts.register(user_data)
                exit()
            elif account_bar == "n":
                exit()
            else:
                print("\033[31;1mAccount [%s] 账户不存在是否立即注册！（y,n）\033[0m" % account)



def acc_auth2(account,password):
    '''
    数据库认证接口
    :param account: 认证账号
    :param password: 认证密码
    :return: 认证通过返回账号对象，认证不通过返回null

    '''
    db_api = db_handler.db_handler()
    data = db_api("select * from accounts where account=%s" % account)


    if data['password'] == password:
        exp_time_stamp = time.mktime(time.strptime(data['expire_date'], "%Y-%m-%d"))
        if time.time() > exp_time_stamp:
            print("\033[31;1mAccount [%s] has expired,please contact the back to get a new card!\033[0m" % account)
        else:  # passed the authentication
            return data
    else:
        print("\033[31;1mAccount ID or password is incorrect!\033[0m")

def acc_login(user_data,log_obj):
    '''
    该函数实现用户登录功能
    :user_data: 用户保存在内存中的数据
    :return:
    '''

    retry_count = 0
    while user_data['is_authenticated'] is not True and retry_count < 3 :
        account = input("\033[32;1msaccount:\033[0m").strip()
        password = input("\033[32;1mpassword:\033[0m").strip()
        auth = acc_auth(user_data,account, password)
        if auth: #not None means passed the authentication
            user_data['is_authenticated'] = True
            user_data['account_id'] = account
            #print("welcome")
            return auth
        retry_count +=1
    else:
        log_obj.error("account [%s] too many login attempts" % account)
        exit()