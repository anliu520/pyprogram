#Author:Anliu
import json
import goods_fun

def open_goods_list():
    '''
    该函数功能是实现从文件中获取商品信息
    :return: 商品信息
    '''
    with open('sp','r',encoding='utf-8') as l:
        goods_list = json.load(l)
    return goods_list

dic_key = {}
def menu1():
    print("一级菜单".center(40,"-"))
    dic_key.clear()
    goods_list = open_goods_list()
    for index1,key1 in enumerate(goods_list.keys(),1):
        print(index1,key1)
        dic_key[str(index1)] = key1
    choose = input("y修改商品名字|b回退|q退出>>>'")
    if choose == 'q':
        quit()
    elif choose == "b":
        pass
    elif dic_key.get(choose):
        menu2(dic_key[choose])
    elif choose == "y":

        #调函数修改商品名
        goods_fun.mod_goods_name(dic_key)
    else:
        print('请输入正确的商品')

def menu2(choose1):
    print('二级菜单'.center(40,"-"))
    dic_key.clear()
    goods_list = open_goods_list()
    for index2,key2 in enumerate(goods_list[choose1],1):
        print(index2,key2)
        dic_key[str(index2)] = key2
    choose2 = input("y修改商品名字|b回退|q退出>>>'")

    if choose2 == "q":
        quit()
    elif choose2 == "b":
        menu1()
    elif dic_key.get(choose2):
        menu3(choose1,dic_key[choose2])
    elif choose2 == "y":

        #调函数修改商品名
        goods_fun.mod_goods_name(dic_key)
    else:
        print('请输入正确的商品')
        menu2(choose1)

def menu3(choose1,choose2):
    print('三级菜单'.center(40,'-'))
    dic_key.clear()
    goods_list = open_goods_list()
    for index3,key3 in enumerate(goods_list[choose1][choose2],1):
        print(index3,key3, goods_list[choose1][choose2][key3])
        dic_key[str(index3)] = key3
    choose3 = input('y修改商品名字|m修改商品价格|b回退|q退出>>>')
    if choose3 == "q":
        quit()

    elif choose3 == "b":
        menu2(choose1)

    elif choose3 == "y":
        #调函数修改商品名
        goods_fun.mod_goods_name(dic_key)

    elif choose3 == "m":
        #调函数修改商品价格
        goods_fun.mod_goods_price(goods_list[choose1][choose2])
    else:
        print('请输入正确的商品')
        menu3(choose1,choose2)

def main():
    while True:
        menu1()
