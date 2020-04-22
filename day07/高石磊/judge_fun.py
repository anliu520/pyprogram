#Author:Anliu
import json
import shopping_register
import shopping_logging
import goods_mod
import goods_fun

def judge_for_pass(sf):
    '''
    该函数功能是实现判断用户是否认证成功。
    :param sf: 用户类别，gly表示管理员，user表示普通用户
    :return: 返回值为0或者1，1表示认证通过，0表示认证不通过。
    '''

    with open('user', 'r') as f:
        ul = json.load(f)
    username_and_password = shopping_logging.input_massage()  # 调用用户输入函数
    back_flag = shopping_logging.check_account(username_and_password, ul[sf], ul[sf][username_and_password[0]])
    return back_flag

def judge_admin_fun(admin_fun_bar):
    '''
    该函数功能判断管理员需要执行的方法
    :param admin_fun_bar: 用户输入的方法，x表示修改，g表示购买
    :return:
    '''

    if admin_fun_bar == "x":
        goods_mod.main()
    elif admin_fun_bar == "g":
        goods_fun.buy_goods()
    else:
        print('请输入正确的操作')

def judge_user_fun():
    '''
    该函数功能实现用户的方法
    :return:
    '''

    goods_fun.buy_goods()


def judge_for_user(user_bar):

     if judge_for_pass(user_bar):
         if user_bar == "gly":

             admin_fun_bar = input('x修改商品信息|g购买物品>>>')
             judge_admin_fun(admin_fun_bar)

         elif user_bar == "user":

             judge_user_fun()
         else:
             print("请输入正确的身份")
     else:
         print("认证不通过！！！检查账号密码")


def judge_for_account(account_bar):
    '''
    该函数功能是为了实现根据用户的输入判断下一步的操作，
    用户输入的值通过传参的方式传递到此函数，
    用户输入的值：y表示有账号，n表示没有账号，q表示退出。
    :param account_bar: 用户输入的动作
    :return:
    '''
    if account_bar == "y":
        user_bar = input('请输入您的身份(gly(管理员)|user(用户)):')
        judge_for_user(user_bar)
    elif account_bar == "n":
        shopping_register.register()
    elif account_bar =="q":
        exit()
    else:
        print("请输入正确的操作...")
