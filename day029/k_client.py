#Author:Anliu
import paramiko
#定义私钥位置
private_key = paramiko.RSAKey.from_private_key_file(r'C:\Users\My\.ssh\linux\id_rsa')

#创建SSH对象
ssh = paramiko.SSHClient()
#容许链接不在know_hosts文件中的主机
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#链接服务器
ssh.connect(hostname="192.168.42.3",port=22,username="root",pkey=private_key)
print("------链上了-----")

#执行指令
stdin,stdout,stderr = ssh.exec_command("df")
#result = stdout.read()
res,err = stdout.read(),stderr.read()
result = res if res else err
print(result.decode())

#关闭链接
ssh.close()
