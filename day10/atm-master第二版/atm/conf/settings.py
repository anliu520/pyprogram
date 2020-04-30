#Author:Anliu

import os,sys,logging

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#print(BASE_DIR)

DATABASE = {
    'engine': 'file_storage', #support mysql,postgresql in the future/mysql/sqlit
    'role': 'user',
    'name': 'accounts',
    'path': "%s/db/accounts/" % BASE_DIR,
    'admin_path': "%s/db/admin/" % BASE_DIR
}

LOG_LEVEL = logging.INFO


LOG_TYPES = {
    'transaction': 'transactions.log',
    'access': 'access.log',
}

ACCOUNT_TYPE = {
    "role":"",
    "username": "1",
    "password": "1",
    "balance": 20363.0,
    "limit": 20000,
    "frozon": False,
    "expire_date": "2022-01-01",  #添加格式  2021-01-01
    "enroll_date": ""
}



TRANSACTION_TYPE = {
    'repay':{'action':'plus', 'interest':0},
    'withdraw':{'action':'minus', 'interest':0.05},
    'transfer':{'action':'minus', 'interest':0.05},
    'consume':{'action':'minus', 'interest':0},
}

