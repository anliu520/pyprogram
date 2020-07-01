#Author:Anliu

#Author:Anliu
class test():
    '''
    The class implements the login function
    '''
    def __init__(self,name):
        self.name = name

    def login(self):
        print("login...")

    def __call__(self, *args, **kwargs):  #定义__call__方法
        print(args,kwargs)

    def __str__(self):
        return "anliu"

    def __getitem__(self, item):
        print('__getitem__',item)

    def __setitem__(self, key, value):
        print('__setitem__',key,value)

    def __delitem__(self, key):
        print('__delitem__',key)


#fun1 = test("anliu")
#result = fun1["k1"]   #__getitem__ k1
#fun1["k1"] = "v1"  #__setitem__ k1 v1
#del fun1["k1"]
##fun1["k1"]
