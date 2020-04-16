#Author:Anliu
import json

dict = {"linux1921":["dongyu","tongtong","yaobin"]} # 内存

with open("test","w") as f:
    json.dump(dict,f)