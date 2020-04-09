#Author:Anliu
f = open("test","r",encoding="utf-8")
#print(f.write("this is a test "))
#print(f.read())
#for i in range(5):
#    print(f.readline().strip())
'''
print(f.readlines())
print(f.readlines())
print(f.readlines())
'''
#for index,itme in enumerate(f.readlines()):
#    if index == 3:
#        continue
#    print(index,itme.strip())

#print(i.strip())
'''
对比：
file 8G
f.readline  ：读出所有内容。一句一句读。  ------多内容
f.readlines  ：读出错有内容，每一句内容当做列表的元素。读出所有。  -----小文件
没法实现协程，程序一旦运行，将不会中断。
'''
#for i in f:
#    print(i.strip())
'''
本身是迭代器方法。程序运行可以中断。可以实现协程
'''
print(f.fileno())  #文件句柄标号（操作系统）
print(f.readline().strip())
print(f.tell())  #20
print(f.read(3))  #
print(f.tell())   #29 ==20+3x3
f.seek(3)  # 3字符 = utf-8 1汉字，从开头计算
print(f.read(3))  # 3个汉字
print(f.fileno())

print("-------------it's fenggexian--------------")
for i  in range(10):
    print(f.readline().strip())
print("-------------it's fenggexian--------------")
print(f.tell())
print(f.fileno())
print(f.readline().strip())
print(f.fileno())
print(f.readable())  #tty,设备文件，不可读
print(f.seekable())
