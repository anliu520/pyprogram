#Author:Anliu

import yaml,json

with open("parameter","r",encoding="utf-8") as f2:
    parameter = json.load(f2)

with open("pod_list.yaml","r",encoding="utf-8") as f1:
    #print()   # 1__next__():
    text1 = yaml.load(f1,Loader=yaml.FullLoader)  #2_next__()
    print(type(text1))
    print(text1["apiVersion"])
    #text1["apiVersion"] = "v2"
    text1["apiVersion"] = input("[apiVersion]:%s >>>:"%parameter["apiVersion"])
    #text1["kind"] = "Deployment"
    text1["kind"] = input("[kind]: %s >>>:"%parameter["kind"])
    text1["metadata"]["name"] = "python_app"
    print(text1["metadata"]["labels"])
    text1["metadata"]["labels"].update({"app":"python_app","version":"v2"})
    text1["spec"]["containers"][0]["name"] = "python-app"
    text1["spec"]["containers"][0]["image"] = "image"
    print(text1)

with open("pod_list_bak.yaml","w",encoding="utf-8") as f2:
    yaml.dump(text1,f2)