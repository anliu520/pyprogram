#Author:Anliu
import configparser
config = configparser.ConfigParser()
config["DEFAULT"] = {'server_host':"DNS01",
                     'server_ip':"0.0.0.0",
                     "server_path":"/data"
                     }
config["user"] = {}  #添加空节点
config["user"]["name"] = 'root'   #给节点添加键值

config["pass"] = {}
tops = config["pass"]
tops["password"] = "123456"
tops["pass_key"] = "/root/.ssh/key.pub"

config['DEFAULT']["server_socket"] = "/lib/dns.sock"



with open("named.conf","w",encoding="utf-8") as cpfile:
    config.write(cpfile)
