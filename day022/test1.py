#Author:Anliu
#Author:Anliu
import re
class JudgeRegule:
    a = "123"
    list = []
    def __init__(self,name):   #  构造函数:实例化时做初始化的工作
        self.name = name      #实例变量（静态属性）

    def judge_IP(self,paramater):   #类方法（动态属性）
        pat = "^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"
        patobj = re.compile(pat)
        #if patobj.search(data):
        print("IP:",self.name)
        if patobj.search(paramater):
            return True
        else:
            return False

    def judge_MAC(self,parameter):
        valid = re.compile(r'''
                              (^([0-9A-F]{1,2}[-]){5}([0-9A-F]{1,2})$
                              |^([0-9A-F]{1,2}[:]){5}([0-9A-F]{1,2})$
                              |^([0-9A-F]{1,2}[.]){5}([0-9A-F]{1,2})$)
                              ''',
                            re.VERBOSE | re.IGNORECASE)
        #re.IGNORECASE的意思就是忽略大小写
        #re模块的re.VERBOSE可以把正则表达式写成多行，并且自动忽略空格。
        print("MAC:",self.name)
        return valid.match(parameter) is not None

#print(JudgeRegule.a)

r1 = JudgeRegule("判断结果是：")   #实例化
print(r1.a)   #查
r1.a = "456"  #改
print(r1.a)
print("r1 修改前",r1.list)
r1.list.append("aaa")
print("r1 修改后",r1.list)


#print(r1.judge_IP("192.168.42.1"))
#print(r1.judge_MAC("00:0c:29:06:be:2f"))
#print(r1.name)      #查看
#r1.name = "xxxxx"  #修改
#print(r1.name)
#del r1.name         #删除
#print(r1.name)
#r1.password = "123456" #增
#print(r1.password)

r2 = JudgeRegule("judge of res:")
print(r2.a)
print("r2:",r2.list)
#print(r2.judge_IP("192.168.42.32"))
#print(r2.judge_MAC())

