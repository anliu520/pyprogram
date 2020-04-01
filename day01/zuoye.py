#Author:Anliu
import getpass
_username = "anliu"
_password = "123"
num = 0
while num <3:
    username = input("username:")
    # password = getpass.getpass("password:")
    password = input("password:")
    if _username == username and _password == password:
        print("欢迎您登陆...")
        exit()
    else:
        print("账号或者密码错误")
    num +=1
else:
    print("账号已锁定，请联系管理员开通")

