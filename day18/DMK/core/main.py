#Author:Anliu
from core import auth

user_data = {
    'account_id':None,
    'is_authenticated':True,
    'account_data':None
}

def print_change_record():
    pass

def add_change_account():
    pass

def add_change_node():
    pass

def test_change_node_conn():
    pass

def modify_hosts_conf():
    pass

def modify_var():
    pass

def upgrade():
    pass

def rollback():
    pass



def logout():
    exit()


def interactive(acc_data):
#    print(user_data)
    '''
    interact with user
    :return:
    '''
    menu = u'''
    ------- 功能菜单 ---------
    \033[32;1m
    1.  打印变更记录
    2.  添加变更账号
    3.  添加变更节点
    4.  测试变更节点连通性
    5.  修改hosts配置
    6.  修改变量
    7.  升级
    8.  回滚
    9.  退出
    \033[0m'''
    menu_dic = {
        '1': print_change_record,
        '2': add_change_account,
        '3': add_change_node,
        '4': test_change_node_conn,
        '5': modify_hosts_conf,
        '6': modify_var,
        '7': upgrade,
        '8': rollback,
        '9': logout
    }
    exit_flag = False
    while not exit_flag:
        print(menu)
        user_option = input(">>:").strip()
        if user_option in menu_dic:
            menu_dic[user_option]()
        else:
            print("\033[31;1mOption does not exist!\033[0m")

def running():
    #print("This is a running...")
    acc_data = auth.account_loggin()
#    print(acc_data)
    if user_data['is_authenticated']:
        user_data['account_data'] = acc_data[0]
        user_data['account_id'] = acc_data[1]
        interactive(user_data)  # 交互

