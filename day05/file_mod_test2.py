#Author:Anliu
import sys

a = sys.argv[1]
b = sys.argv[2]
#print(a, b)

f = open("named.conf", mode="r", encoding="utf-8")
f_new = open(".named.conf.swp","w",encoding="utf-8")
for line in f:
    if "listen-on " in line:
        line = line.replace(a,b)
#    print(line)
    f_new.write(line)
f_new.flush()
f_new.close()
f.flush()
f.close()

f = open("named.conf", mode="w", encoding="utf-8")
f_new = open(".named.conf.swp","r",encoding="utf-8")
for line_new in f_new:
#    print(line_new)
    f.write(line_new)
f_new.close()
f.flush()
f.close()
#    print
