#Author:Anliu
import hashlib

def desc_auth(bar):
    '''
    装饰器实现对hashlib的加密接口输出形式的判断与呈现。
    :param bar:
    :return:
    '''

    def run(data,type):
        cret = bar(data,type)   #md5()
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
def md5(data,type):
    '''
    实现md5的加密接口
    :param data:
    :param type:
    :return:
    '''
    cret = hashlib.md5()
    cret.update(data.encode("utf-8"))
    return cret

print(md5("admin","digest"))

@desc_auth
def sha1(data,type):
    '''
    实现sha1的加密接口
    :param data:
    :param type:
    :return:
    '''

    cret = hashlib.sha1()
    cret.update(data.encode("utf-8"))
    return cret

print(sha1("admin","hexdigest"))

@desc_auth
def sha256(data,type):
    '''
    实现sha256的加密接口
    :param data:
    :param type:
    :return:
    '''
    cret = hashlib.sha256()
    cret.update(data.encode("utf-8"))
    return cret

print(sha256("admin", "hexdigest"))

@desc_auth
def sha384(data,type):
    '''
    实现sha384的加密接口
    :param data:
    :param type:
    :return:
    '''
    cret = hashlib.sha384()
    cret.update(data.encode("utf-8"))
    return cret

print(sha384("admin", "hexdigest"))

@desc_auth
def sha512(data,type):
    '''
    实现sha512的加密接口
    :param data:
    :param type:
    :return:
    '''
    cret = hashlib.sha512()
    cret.update(data.encode("utf-8"))
    return cret

print(sha512("admin", "hexdigest"))
