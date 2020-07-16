#Author:Anliu

import paramiko
#实例化一个SSH客户端对象
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)

ssh.connect(hostname="192.168.42.3",port="22",username="root",password="123456")
print("---------链接上了---------")
while True:
    cmd = input(">>>")
    stdin,stdout,stderr = ssh.exec_command(cmd)
    #print(stdin.decode())
    out,err = stdout.read(),stderr.read()
    res = out if out else err
    print(res.decode())
    #print(stdout.read().decode())
    #print(stderr.read().decode())