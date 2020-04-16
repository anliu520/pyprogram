#Author:Anliu
f = open("test","r")
#print(f.read())
#print(f.readline())
#print(f.readlines())  # 小文件
#for i in f:  #迭代器
#    print(i)

#print(f.tell())
#print(f.read(1))
#f.seek(3)
#print(f.tell())
#print(f.fileno())
#f1 = open("test_file1.py","r")
#print(f1.fileno())
#print(f1.readable())
#f1.flush()   #强制实时刷新

f2 = open("test1","a")
f2.write("this is a test ..")
f2.write("this is a test1 ..")


