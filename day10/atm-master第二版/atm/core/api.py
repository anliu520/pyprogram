#Author:Anliu
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author aliex-hrg.json
import os,json,time
from conf import settings

def auth(fun):
    '''
    装饰器实现对ATM的每个功能添加认证
    :param fun: 被装饰函数的内存地址对象
    :return: null
    '''

    def target(acc_data):
        if acc_data["is_authenticated"]:
            fun(acc_data)
        else:
            print("认证失败，请检查登录")
    return target

@auth
def add(acc_data):
    '''
    该函数实现用户注册账号功能，账号注册在文件中，每个账号对应一个文件。
    :return:
    '''
    if acc_data["account_role"] == "user":
        print("您不是admin，%s用户角色不能创建user")
        exit()
    username = input("请输入用户名：")
    if not os.path.isfile(settings.DATABASE["path"] + username + '.json'):
        passwd = input("请输入密码：")
        balance = int(input("请输入存款金额："))
        limit = int(input("请设置信用额度："))
        info = settings.ACCOUNT_TYPE
        info.update({'username':username,'password':passwd,'balance':balance,'limit':limit})
        changeuserinfo(username,info)
        log = "添加用户"+username
    else:
        print("添加的用户已经存在")
        log = "添加用户失败，用户已经存在"
    writeatmlog(log)

@auth
def select(acc_data):
    '''
    提供用户查询接口。
    :return: null
    '''
    user = input("请输入要查询的用户>>:")
    #print(settings.DATABASE["path"])
    if os.path.isfile(settings.DATABASE["path"]+user+'.json'):
        #os.path.isfile(BASE_DIR + '\\accounts\\' + user + '.json')
        for i in getuserinfo(user):
            print(i,"\t:\t",getuserinfo(user)[i])
        #print(getuserinfo(user))
        log = "查询到此用户："+user
    else:
        print("查无此用户")
        log = "查询"+user+"用户，没有结果"
    writeatmlog(log)

@auth
def remove(acc_data):
    '''
    用户以及日志信息删除。
    :return:
    '''

    username = input("请输入你要注销的用户：").strip()
    if os.path.isfile(settings.DATABASE["path"]+username+'.json'):
        os.remove(settings.DATABASE["path"]+username+'.json')
        print("注销用户%s成功" %username)
        writeatmlog("注销用户%s成功" %username)
    else:
        print("你输入的用户不存在")
        writeatmlog("你输入的用户%s不存在" %username)

    #if os.path.isfile(BASE_DIR + '/logs/' + username + '.log'):
    #    os.remove(BASE_DIR + '/logs/' + username + '.log')
    #    print("删除用户%s的日志成功" %username)
    #    writeatmlog("删除用户%s的日志成功" %username)

@auth
def transfer(acc_data):
    '''
    该函数实现转账功能。
    :return:
    '''

    print("\t\t转账系统")
    #fromusername = input("请输入转账人用户名：").strip()
    #passwd = input("请输入转账人密码：").strip()
    fromuser = getuserinfo(acc_data["account_id"])
    if fromuser["frozon"]:
        print("%s用户已经被冻结"%acc_data["account_id"])
        writeatmlog("%s用户已经被冻结,不支持转出"%acc_data["account_id"])
        return "fail"

    tousername = input("请输入转入方账号：").strip()
    touser = getuserinfo(tousername)
    if touser["frozon"]:
        print("%s用户已经被冻结" %tousername)
        writeatmlog("%s用户已经被冻结,不支持转入" %tousername)
        return "fail"

    tonum = int(input("请输入转入金额："))
    if fromuser["balance"] - tonum < - fromuser["limit"]:
        print("你的信用额度不够，少转点。")
        writeatmlog("%s转账给%s失败，可用额度不够" %(acc_data["account_id"],tousername))
        return "fail"
    else:
        fromuser["balance"] -= tonum
        touser["balance"] += tonum
        changeuserinfo(tousername,touser)
        changeuserinfo(acc_data["account_id"],fromuser)
        writeatmlog("%s用户转账给%s用户%s元成功" %(acc_data["account_id"],tousername,tonum))
        print("转入成功")

@auth
def withdraw(acc_data):
    '''
    该函数实现提现功能。
    :return:
    '''

    print("\t\t提现系统")
    #username = input("请输入用户名：").strip()
    #passwd = input("请输入密码：").strip()
    fromuser = getuserinfo(acc_data["account_id"])
    if fromuser["frozon"]:
        print("%s用户已经被冻结"%acc_data["account_id"])
        writeatmlog("%s用户已经被冻结,不支持提现"%acc_data["account_id"])
        return "fail"
    #if passwd == fromuser["password"]:
    #    print("登录成功，%s，欢迎你" %username)
    bill = int(input("请输入提现金额："))
    if fromuser["balance"] - bill < - fromuser["limit"]:
        print("你的提现额度超过信用额度了。")
        writeatmlog("%s提现%s元失败，可用额度不够" %(acc_data["account_id"],bill))
    else:
        fromuser["balance"] = fromuser["balance"] - bill - bill*5/100
        changeuserinfo(acc_data["account_id"],fromuser)
        writeatmlog("%s提现%s元成功" %(acc_data["account_id"],bill))
        print("提现成功")

@auth
def frozen(acc_data):
    '''
    实现用户账户冻结或解冻
    :return: null
    '''

    print("\t\t冻结系统")
    username = input("请输入要操作的用户名：").strip()
    act = input("冻结按1，解冻按2").strip()
    fromuser = getuserinfo(username)
    if act == "1":
        fromuser["frozon"] = True
        log = "冻结%s用户成功" %username
    elif act == "2":
        fromuser["frozon"] = False
        log = "解冻%s用户成功" %username
    else:
        print("输入有误")
        return "fail"
    changeuserinfo(username,fromuser)
    print(log)
    writeatmlog(log)

@auth
def repayment(acc_data):
    '''
    提供还款接口。
    :return:
    '''

    print("\t\t还款系统")
    #username = input("请输入用户名：").strip()
    #passwd = input("请输入密码：").strip()
    print(acc_data["account_id"])
    fromuser = getuserinfo(acc_data["account_id"])
    #if passwd == fromuser["password"]:
    #    print("登录成功，%s，欢迎你" %username)
    balance = fromuser["balance"]
    if balance > 0:
        print("你目前的余额为%s元,不需要还款" %balance)
        return "do not repayment"
    else:
        print("你目前的余额为%s元,需要还款%s元" %(balance,abs(balance)))
        bill = int(input("请输入要还款的金额："))
        fromuser["balance"] = fromuser["balance"] + bill
        changeuserinfo(acc_data["account_id"],fromuser)
        writeatmlog("%s还款%s元成功" %(acc_data["account_id"],bill))
        print("还款成功")


def printbill(acc_data):
    '''
    实现账单打印接口，。用户输入账单的起始和结束日期，即可打印对应日志。
    :return: null
    '''

    print("\t\t打印账单系统")
    #username = input("请输入用户名：").strip()
    #passwd = input("请输入密码：").strip()
    #fromuser = getuserinfo(acc_data["account_id"])
    #if passwd == fromuser["password"]:
    #    print("登录成功，%s，欢迎你" %username)
    date1 = input("输入打印账单开始日期,格式:2020-04-03 12:00:00>>>:")
    date2 = input("输入打印账单结束日期,格式:2020-04-03 20:00:00>>>:")
    with open(settings.BASE_DIR + '/log/atm.log','r',encoding='utf8') as f:
        for i in f:
            if i[:19] >= date1 and i[:19] < date2:
                print(i.strip())
    writeatmlog("打印用户%s的账单%s到%s" %(acc_data["account_id"],date1,date2))

@auth
def api_payment(user,num):
    '''
    改函数功能是让购物车调用的扣款接口。
    :param user: 扣款用户
    :param num: 扣款金额
    :return: 若扣款失败，返回fail，具体原因查看日志；若扣款成功，返回用户的预算
    '''

    info = getuserinfo(user)
    if info["frozon"]:
        print("%s用户已经被冻结"%user)
        writeatmlog("%s用户已经被冻结,支付失败"%user)
        return "fail"
    if info["balance"] - int(num) < - info["limit"]:
        print("超过信用卡透支额度，无法购买")
        writeatmlog("%s购物支付失败" %user)
        return "fail"
    else:
        info["balance"] -= int(num)
    changeuserinfo(user,info)
    writeatmlog("%s用户购物支付成功" %user)
    return info["balance"]

def getuserinfo(user):
    '''
    该函数功能是获取指定用户的json信息。
    :param user: 用户名
    :return: 返回用户注册的整个文件
    '''

    if os.path.isfile(settings.DATABASE["path"]+user+'.json'):
        with open(settings.DATABASE["path"]+user+'.json','r',encoding='utf8') as f1:
            temp = json.loads(f1.read())
        return temp
    else:
        print("此用户不存在！请确认输入")

def changeuserinfo(user,changeinfo):
    '''
    改函数功能提供修改用户信息接口。
    :param user: 用户名
    :param changeinfo: 整个用户信息的内容
    :return: null
    '''

    with open(settings.DATABASE["path"] + user + '.json', 'w', encoding='utf8') as f1:
        f1.write(json.dumps(changeinfo))

def writeatmlog(lines):
    '''
    该函数提供日志写入接口。
    :param lines: 需要虚入的内容
    :return: null
    '''

    with open(settings.BASE_DIR + '/log/atm.log','a',encoding='utf8') as f:
        curr_time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
        f.write("%s %s\n" %(curr_time,lines))