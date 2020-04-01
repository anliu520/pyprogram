#Author:Anliu
#a = "abcdefg"
for i in range(1,10):
   #print(i)
   for j in range(1,i+1):
       print("%sx%s=%s" %(i,j,i*j),end=" ")
   print()
