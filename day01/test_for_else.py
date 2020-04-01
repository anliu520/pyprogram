#Author:Anliu
for mun in range(10,20):
    for i in range(2,mun):
        if mun%i == 0:
            break
    else:
        print("质数:%s" %mun)
