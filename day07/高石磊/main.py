#Author:Anliu
import judge_fun
def main():
    while True:
        account_bar = input('是否存在账户密码(y有|n没有并注册|q退出):')
        judge_fun.judge_for_account(account_bar)


'''
对于python脚本：
（1）直接运行
（2）当做模块传递
__name__ == '__main__' 就是将以上两种方式做以区分，
若要当做模块传递，无需定义；
若要直接运行，则需要定义。

从本质上讲：定义了一个程序的总入口。
'''

if __name__ == '__main__':
    main()