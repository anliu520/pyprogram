#Author:Anliu
import yaml

data = '''
- liunx
- hosts
- ip
'''
#print(yaml.load(data,Loader=yaml.FullLoader))

#with open("httpd.yaml","r",encoding="utf-8") as f1:
    #a1 = yaml.load(f1,Loader=yaml.FullLoader)
    #a2 = yaml.load_all(f1,Loader=yaml.FullLoader)
    #print(type(a1),type(a2))
    #for i in a2:
    #    print(i[0].get("hosts"))

dict = {
    "name":"anliu",
    "age":18,
    "ip":"192.168.42.111",
    "host":"DNS"
}

with open("test1.yaml","w",encoding="utf-8") as f1:
    yaml.dump(dict,f1)



