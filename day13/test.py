#Author:Anliu
import random
#print(random.randint(1000,9999))
#print(random.randint(0,9))
checkcode = ""
for i in range(5):   # 0-9
    current = random.randint(0,9)
    #checkcode += str(current)
    if current == i:
        tmp = chr(random.randint(65,90))
    else:
        tmp = random.randint(0,9)
    checkcode += str(tmp)
print(checkcode)

#print(chr(100))  #65-90 : 97-122
