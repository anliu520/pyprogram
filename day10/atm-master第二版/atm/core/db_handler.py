#Author:Anliu

'''
handle all the database interactions
'''
#import os
#import sys
#base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#sys.path.append(base_dir)

import json,time ,os
from conf import settings


def file_db_handle(user_data,conn_params):
    '''
    解析数据库文件路径
    :param conn_params: 配置中设置的路径
    :return:
    '''

    print('file db:',conn_params)
    #db_path ='%s/%s' %(conn_params['path'],conn_params['name'])
    #return file_execute
    if user_data["account_role"] == "user":
        return conn_params["path"]
    elif user_data["account_role"] == "admin":
        return conn_params["admin_path"]
    else:
        print("角色不对..")
#file_db_handle(settings.DATABASE)



def db_handler(user_data):
    '''
    链接数据库
    :param conn_parms: db链接的参数来自于数据库
    :return:a
    '''

    conn_params = settings.DATABASE
    if conn_params['engine'] == 'file_storage':
        return file_db_handle(user_data,conn_params)
    elif conn_params['engine'] == 'mysql':
        pass



def file_execute(sql,**kwargs):
    conn_params = settings.DATABASE
    db_path = '%s/%s' % (conn_params['path'], conn_params['name'])

    print(sql,db_path)
    sql_list = sql.split("where")
    print(sql_list)
    if sql_list[0].startswith("select") and len(sql_list)> 1:#has where clause
        column,val = sql_list[1].strip().split("=")

        if column == 'account':
            account_file = "%s/%s.json" % (db_path, val)
            print(account_file)
            if os.path.isfile(account_file):
                with open(account_file, 'r') as f:
                    account_data = json.load(f)
                    return account_data
            else:
                exit("\033[31;1mAccount [%s] does not exist!\033[0m" % val )

    elif sql_list[0].startswith("update") and len(sql_list)> 1:#has where clause
        column, val = sql_list[1].strip().split("=")
        if column == 'account':
            account_file = "%s/%s.json" % (db_path, val)
            #print(account_file)
            if os.path.isfile(account_file):
                account_data = kwargs.get("account_data")
                with open(account_file, 'w') as f:
                    acc_data = json.dump(account_data, f)
                return True