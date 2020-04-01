#Author:Anliu
print('|---新建用户：N/n---|')
print('|---登录账号：E/e---|')
print('|---退出程序：Q/q---|')
contact = dict()
while 1:
    a = input('请输入指令代码：')

    if a == 'N' or a == 'n':
        name = input('请输入用户名：')
        if name in contact:
            name = input('此用户已经被使用，请重新输入：')
            continue
        else:
            mima = input('请输入密码：')
            contact['name'] = mima
            print('注册成功，请登录！')

    if a == 'E' or a == 'e':
        name = input('请输入用户名：')
        if name not in ['name']:
            print('您输入的用户名不存在，请重新输入：')
            continue
        else:
            mima = input('请输入密码：')
            mima1 = contact['name']
        if mima1 == mima:
            print('欢迎进入xx系统，请点击右上角的x结束程序！')
        else:
            print('密码输入错误！')

    if a == 'Q' or a == 'q':
        break