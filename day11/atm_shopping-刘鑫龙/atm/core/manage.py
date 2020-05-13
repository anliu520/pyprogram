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


#temp account data ,only saves the data in memory
user_data = {
    'account_role':"admin",
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
    1.  查看用户信息
    2.  创建用户
    3.  删除用户
    4.  冻结用户
    5.  账单
    6.  退出
    \033[0m'''
    menu_dic = {
        '1': api.select,
        '2': api.add,
        '3': api.remove,
        '4': api.frozen,
        '5': api.printbill,
        '6': logout,
    }
    exit_flag = False
    while not exit_flag:
        print(menu)
        user_option = input(">>:").strip()
        if user_option in menu_dic:
            #print('accdata',acc_data)
            #acc_data['is_authenticated'] = False
            menu_dic[user_option](acc_data)

        else:
            print("\033[31;1mOption does not exist!\033[0m")
def run():
    '''
    这个函数在程序启动时会被正确调用，这里处理用户交互的内容
    :return:
    '''
    acc_data = auth.acc_login(user_data,access_logger)
    if user_data['is_authenticated']:
        user_data['account_data'] = acc_data
        interactive(user_data)
