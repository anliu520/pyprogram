#Author:Anliu

list = ["linux","123","zhangkai","zhangkai","#anliu"]

#list[2] = False
print(list.index("zhangkai"))
print(list.count("zhangkai"))
list.append("tongtong")
#list.clear()
print(list)
#list.pop(list.index("zhangkai"))
#list.reverse()
print(list)
#list.sort()
#list.remove("zhangkai")
list.insert(list.index("tongtong"),"yaobin")
print(list)
#print(list[2])


linux = ["quanquan","dongyu","xinwei"]
java = ["sunhang","luoshuxing","guoxiudu"]
#del linux
print(linux[:2])

for i in linux:
    print(i)


#print(linux)
#linux.extend(java)
#print(linux)

