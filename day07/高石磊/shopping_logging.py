#Author:Anliu

def input_massage():
    '''
    该函函数功能是为了实现统一接受用户输入信息
    :return:返回用户名和密码
    '''
    username = input("username:")
    password = input("password:")
    return username,password

def check_account(*args):
    '''
    该函数功能是实现用户信息认证。
    :return: 信息认证通过返回1，不通过返回0
    '''
    print(args)
    if args[0][0] in args[1] and args[0][1] == args[2]:
        flag = 1
    else:
        flag = 0
    return flag
