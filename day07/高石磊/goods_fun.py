#Author:Anliu
import json

def mod_goods_name(*args):
    '''
    This is function used alter goods
    :return:
    '''
    #print(args)
    ch31 = input('请输入你需要修改的商品代号:')
    ch32 = input('请输入修改后的名字:')
    for i3 in args:
        print(i3)
        i3.update({ch31:ch32})
        print(i3)


def mod_goods_price(*args):
    '''
    该函数功能是实现商品价格的修改
    :param args:
    :return:
    '''
    #print(args)
    for i3 in args:
        print(i3)
        ch33 = input('请输入你需要修改的商品价格的名字:')
        ch34 = str(input('请输入修改后的价格:'))
        i3.update({ch33:ch34})
        print(i3)

def buy_goods():
    '''
    该函数功能是购买商品
    :return:
    '''
    with open('sp', 'r') as n:
        su1 = json.load(n)
        print(su1)
        print("剩下功能自己写...")

def scan_goods():
    '''

    :return:
    '''
    pass