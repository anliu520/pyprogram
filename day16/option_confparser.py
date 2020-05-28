#Author:Anliu
import configparser
config = configparser.ConfigParser()
config.read("named.conf")

sec = config.sections()
print(sec)
#print(config.options("user")) #打印键值，以列表的形式呈现，包括指定的节点以及DEFAULT
#print(config.get("user","name"))  #打印对应节点的key的值。
#print(config.getint("user","name"))

#config.remove_section("user")    #删除节点
#config.write(open("named.conf","w"))

#config.remove_option("pass","pass_key")  #删除键值
#config.write(open("named.conf","w"))
print(config.has_section("user"))

if not config.has_section("user"):  #增加节点
    config.add_section("user")
    config.write(open("named.conf","w"))

#config.set("user","name","root")  #增加键值
#config.write(open("named.conf","w"))

config.set("user","name","admin")  # 修改键的值
config.write(open("named.conf","w"))











