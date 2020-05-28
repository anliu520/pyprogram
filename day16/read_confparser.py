#Author:Anliu
import configparser
config = configparser.ConfigParser()
#print(config.sections())
config.read("named.conf")
print(config.sections())

if 'DEFAULT' in config:
    a = config["DEFAULT"]
    print(a["server_ip"])
else:
    print("NULL")

print(config)
for i in config:
    print(i)

