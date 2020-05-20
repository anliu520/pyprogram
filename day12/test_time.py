#Author:Anliu
import time
#print(time.time())
a = time.time()
c = time.clock()
#print(time.clock())
#print(time.ctime(c))
t = time.gmtime()  #世界协调时间
#print(t)
#print(t.tm_year)
#print(t.tm_yday)
#print(t.tm_mday)
l = time.localtime()  #本地时间
#print(l)

#print(time.mktime(l))

print(time.strftime("%Y --- %m ---- %d",l))
f = time.strftime("%Y --- %m ---- %d",l)
print(time.strptime(f,"%Y --- %m ---- %d"))
u = time.strptime("20080512","%Y%m%d")
print(time.strptime(f,"%Y --- %m ---- %d"))
print(u)
