#Author:Anliu

class AUTH:
    def __init__(self,username,userID,userpass,flag):
        self.username = username
        self.userID = userID
        self.userpass = userpass
        self.flag = flag

    def upload_package(self):
        print("%s zhengzai shangchuang bao ..."%self.username)

    def change(self):
        print("zhengzai biangeng ...." )

    def doze(self):
        print("zhengzai dongjie zhanghao ...%s " %self.flag)

    def undoze(self):
        print("zhengzai jiedong  zhanghao ...")

m1 = AUTH("user1","100011","123456",None)
m1.upload_package()
m1.change()

m2 = AUTH("admin1","100012","123456",None)
m2.doze()
m2.undoze()



#问题：（1）属性没有合法性的校验。
#      （2）对于每一个对象（用户）都可使用所有方法。
#      （3）对于某些条件触发，才可修改的属性，可以直接在参数列表中修改。
#      （4）若要添加与属性相关的其他功能，就要修改每一个方法。
