#Author:Anliu

import hashlib

class auth_run:
    '''
    定义父类实现对hashlib的加密接口输出形式的判断与呈现。
    '''

    def desc(self,type,cret):
        list = ["digest", "hexdigest"]
        if type in list:
            if type == list[0]:
                flag1 = cret.digest()
                print(flag1)
            elif type == list[1]:
                flag2 = cret.hexdigest()
                print(flag2)
        else:
            print("Invalid parameter...")

class auth:
    '''
    定义子类实现加密接口
    '''

    def __init__(self,data,type):
        #auth_run.__init__(self,cret)
        self.data = data
        self.type = type
        #self.cret = cret

    def md5(self):
        cret = hashlib.md5()
        cret.update(self.data.encode("utf-8"))
        auth_run.desc(self,self.type,cret)

    def sha1(self):
        cret = hashlib.sha1()
        cret.update(self.data.encode("utf-8"))
        auth_run.desc(self,self.type,cret)

    def sha256(self):
        cret = hashlib.sha256()
        cret.update(self.data.encode("utf-8"))
        auth_run.desc(self,self.type,cret)

    def sha384(self):
        cret = hashlib.sha384()
        cret.update(self.data.encode("utf-8"))
        auth_run.desc(self,self.type,cret)

    def sha512(self):
        cret = hashlib.sha512()
        cret.update(self.data.encode("utf-8"))
        auth_run.desc(self,self.type,cret)

m1 = auth("admin","hexdigest")
m1.md5()
m1.sha1()
m1.sha256()
m1.sha384()
m1.sha512()