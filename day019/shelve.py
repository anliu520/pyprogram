#Author:Anliu

import shelve,time
d = shelve.open("file")
list = ["linux",["base","auto"]]
d["name"] = "anliu"
d["list"] = list
d["time"] = time.localtime()

print(d.get("list"))
print(d.get("name"))

