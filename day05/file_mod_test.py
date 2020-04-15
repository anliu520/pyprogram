#Author:Anliu
'''
(1)打开文件---修改
(2)打开文件 ---生成新文件  ----新文件替换旧文件
'''

f = open("named.conf", mode="r", encoding="utf-8")
f_new = open(".named.conf.swp","w",encoding="utf-8")
for line in f:
    if "listen-on " in line:
        line = line.replace("192.168.42.110","192.168.42.111")
    print(line)
    f_new.write(line)
f_new.flush()
f_new.close()
f.flush()
f.close()

f = open("named.conf", mode="w", encoding="utf-8")
f_new = open(".named.conf.swp","r",encoding="utf-8")
for line_new in f_new:
    print(line_new)
    f.write(line_new)
f_new.close()
f.flush()
f.close()
#    print(line)