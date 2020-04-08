#Author:Anliu
import copy
list1 = ["001","linux",["name","anliu"]]
print(list1)
#方法一
#list2 = list1.copy()
#list3 = list1.copy()
#list2[0] = "002"
#list2[2][1] = "zhangkai"
#print(list2)
#print(list3)
#print(list1)
list3 = copy.deepcopy(list1)
list4 = copy.deepcopy(list1)
print(list3)
print(list4)
list3[0] = "002"
list3[2][1] = "zhangkai"
print(list3)
print(list4)



##方法二
#list3 = copy.copy(list1)
#print(list3)
##方法三
#list4 = list1[:]
#print(list4)
##方法四
#list5 = list(list1)
#print(list5)