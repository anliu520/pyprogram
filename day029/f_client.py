#Author:Anliu
import os
remote = "/root/"
local_path = r"K:/myprogram/pyprogram/day029/"

import paramiko
tran =  paramiko.Transport(("192.168.42.3",22))
tran.connect(username="root",password="123456")
sftp = paramiko.SFTPClient.from_transport(tran)

#sftp.put(os.path.join(local_path,"paramiko-2.7.zip"),os.path.join(remote,"123.py"))
sftp.get(os.path.join(remote,"pycrypto-2.6.tar.gz"),os.path.join(local_path,"pycrypto.tar.gz"))
