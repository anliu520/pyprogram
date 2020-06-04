#Author:Anliu
import json

dict = {
    "apiVersion":["v1","apps/v1","rbac.authorization.k8s.io/v1beta1"],
    "kind":["Pod","Deployment","ConfigMap"],
    "labels":{"key1":"volume1","key2":"volume2"}
    #.....
}

def file_out():
    with open("parameter","w",encoding="utf-8") as f1:
        json.dump(dict,f1)

file_out()

def file_radis():
    pass