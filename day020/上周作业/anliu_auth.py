#Author:Anliu
import hashlib

def run(type,cret):
    '''
    实现输出格式的统一定义
    :param type:  输出的数据形式
    :param cret:  生成的加密对象
    :return: 对应形式的加密码
    '''

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

def md5(data,type):
    '''
    实现md5的加密接口
    :param data:  传入得加密数据
    :param type:  输出的数据形式
    :return: 加密后的对应数据形式
    '''

    cret = hashlib.md5()
    cret.update(data.encode("utf-8"))
    flag = run(type,cret)
    return flag

def sha1(data,type):
    '''
    实现sha1的加密接口
    :param data:
    :param type:
    :return:
    '''

    cret = hashlib.sha1()
    cret.update(data.encode("utf-8"))
    flag = run(type,cret)
    return flag

def sha256(data,type):
    '''
    实现sha256的加密接口
    :param data:
    :param type:
    :return:
    '''
    cret = hashlib.sha256()
    cret.update(data.encode("utf-8"))
    flag = run(type, cret)
    return flag

def sha384(data,type):
    '''
    实现sha384的加密接口
    :param data:
    :param type:
    :return:
    '''

    cret = hashlib.sha384()
    cret.update(data.encode("utf-8"))
    flag = run(type, cret)
    return flag

def sha512(data,type):
    '''
    实现sha512的加密接口
    :param data:
    :param type:
    :return:
    '''

    cret = hashlib.sha512()
    cret.update(data.encode("utf-8"))
    flag = run(type, cret)
    return flag