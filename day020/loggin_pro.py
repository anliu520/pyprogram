#Author:Anliu
#变更管理工具

#输入和验证
#"品类 （用户）"
#属性：用户名，用户ID，密码，密码过期时间,触发冻结的标志

#第一类用户
#user: ---> 上传包，执行变更

#第二类用户
#admin： ---> 冻结账号，解冻账号
'''
username1 = input("username:")
userID1 = input("userID:")
userpass1 = input("userpass")

username2 = input("username:")
userID2 = input("userID:")
userpass2 = input("userpass")

username3 = input("username:")
userID3 = input("userID:")
userpass3 = input("userpass")
'''

info = {
    1:{
        "username":"anliu",
        "userID":"10001",
        "userpass":"1234",
        "flag":not None
    },
    2:{
        "username": "admin",
        "userID": "10001",
        "userpass": "1234",
        "flag":None
    }
        }


def auth():
    print(info[2])

auth()


def upload_package():
    a = info[2]["username"]

    print("%s zhengzai shangchuang bao ..."%a)

def change():
    a = info[1]["username"]
    print("%s zhengzai biangeng ...."%a)

def doze():
    a = info[2]["username"]
    print("%s zhengzai dongjie zhanghao ..."%a)

def undoze():
    a = info[2]["username"]
    print("%a zhengzai jiedong  zhanghao ..."%a)


upload_package()
change()

#问题：（1）属性没有合法性的校验。
#      （2）对于每一个对象（用户）都可使用所有方法。
#      （3）对于某些条件触发，才可修改的属性，可以直接在参数列表中修改。
#      （4）若要添加与属性相关的其他功能，就要修改每一个方法。







