#Author:Anliu
import json
def register():
    '''
    This function is to register users
    :return:
    '''
    with open('user', 'r') as f:
        ul = json.load(f)
    username = input('请输入您要注册的username:')
    password = input('请输入您要注册的password:')
    print('注册成功,您现在可以登陆了')
    ul['user'][username]=password
    # print(user1)
    with open('user','w',encoding='utf-8') as f:
        json.dump(ul,f)