#Author:Anliu

'''
 manage program handle module , handle all the manage interaction stuff
'''

from core import auth
from core import accounts
from core import logger
from core import accounts
#from core import transaction
#from core.auth import login_required
from core import api
import time

#transaction logger
trans_logger = logger.logger('transaction')
#access logger
access_logger = logger.logger('access')

user_data = {
    'account_role':"sadmin",
    'account_id':None,
    'is_authenticated':False,
    'account_data':None

}
def logout(acc_data):
    exit()

def interactive(acc_data):
    '''
    用户交互
    :return:
    '''
    menu = u'''
    ------- Bank Of user ---------
    \033[32;1m
    1.  查看管理员信息
    2.  创建管理员
    3.  删除管理员
    4.  冻结管理员
    5.  查看用户信息
    6.  创建用户
    7.  删除用户
    8.  冻结用户
    9.  账单
    0.  退出
    \033[0m'''
    menu_dic = {
        '1': api.s_select,
        '2': api.s_add,
        '3': api.s_remove,
        '4': api.s_frozen,
        '5': api.select,
        '6': api.add,
        '7': api.remove,
        '8': api.frozen,
        '9': api.printbill,
        '0': logout,
    }
    exit_flag = False
    while not exit_flag:
        print(menu)
        user_option = input(">>:").strip()
        if user_option in menu_dic:
            # print('accdata',acc_data)
            # acc_data['is_authenticated'] = False
            menu_dic[user_option](acc_data)

        else:
            print("\033[31;1mOption does not exist!\033[0m")


def run():
    '''
    这个函数在程序启动时会被正确调用，这里处理用户交互的内容
    :return:
    '''
    acc_data = auth.acc_login(user_data, access_logger)
    if user_data['is_authenticated']:
        user_data['account_data'] = acc_data
        interactive(user_data)
