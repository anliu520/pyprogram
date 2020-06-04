#Author:Anliu
import os,sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#print(BASE_DIR)

DATABASE = {
    'engine': 'file_storage', #support mysql,postgresql in the future
    'name':'account',
    'path': "%s/db" % BASE_DIR
}