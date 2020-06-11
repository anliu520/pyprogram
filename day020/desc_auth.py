#Author:Anliu
import hashlib

def desc_auth(fun):  #md5
    '''
    装饰器实现对加密接口返回的数据形式进行判断
    :param fun:
    :return:
    '''
    def run(data,type):
        cret = fun(data,type)    #md5()
        list = ["digest","hexdigest"]
        if type in list:
            if type == list[0]:
                flag1 = cret.digest()
                return flag1
            elif type == list[1]:
                flag2 = cret.hexdigest()
                return flag2
        else:
            print("Invalid parameter...")
    return run

@desc_auth
def md5(data,ypte):
    cret = hashlib.md5()
    cret.update(data.encode("utf-8"))
    return cret

print(md5("admin","hexdigest"))


