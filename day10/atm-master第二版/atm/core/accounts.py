#Author:Anliu
import json,time ,os,sys
from conf import settings
from core import db_handler

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_dir)

def register(user_data):
    '''
    This function is to register users
    :return:
    '''

    dict = settings.ACCOUNT_TYPE
    account = input('请输入您要注册的username:')
    password = input('请输入您要注册的password:')
    if user_data["account_role"] == "user":
        dict.update({'username':account,'password':password,'role':'user'})
    elif user_data["account_role"] == "admin":
        dict.update({'username':account,'password':password,'role':'admin'})

    db_path = db_handler.db_handler(user_data)
    account_file = "%s/%s.json" % (db_path, account)
    print(account_file)

    with open(account_file,'w',encoding="utf-8") as f:
        json.dump(dict,f)

def load_current_balance(account_id):
    '''
    return account balance and other basic info
    :param account_id:
    :return:
    '''
    # db_path = db_handler.db_handler(settings.DATABASE)
    # account_file = "%s/%s.json" %(db_path,account_id)
    #
    db_api = db_handler.db_handler()
    data = db_api("select * from accounts where account=%s" % account_id)

    return data

    # with open(account_file) as f:
    #     acc_data = json.load(f)
    #     return  acc_data
def dump_account(account_data):
    '''
    after updated transaction or account data , dump it back to file db
    :param account_data:
    :return:
    '''

    db_api = db_handler.db_handler()
    data = db_api("update accounts where account=%s" % account_data['id'],account_data=account_data)

    # db_path = db_handler.db_handler(settings.DATABASE)
    # account_file = "%s/%s.json" %(db_path,account_data['id'])
    # with open(account_file, 'w') as f:
    #     acc_data = json.dump(account_data,f)

    return True
