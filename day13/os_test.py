#Author:Anliu
import os
#print(os.getcwd())
#os.chdir("c:")
#print(os.getcwd())
#print(os.curdir)
#print(os.getcwd())
#print(os.pardir)
#os.makedirs(r"c:\a\b\c")
#os.removedirs(r"c:\a\b\c")
#os.mkdir(r"c:\a")
#os.rmdir(r"c:\a")

#print(os.listdir("."))
#os.chdir("c:")
#os.rename("a","b")
#print(os.stat('b'))
#print(os.sep)

#print(os.linesep)
print(os.path.abspath(__file__))  # 获取当前文件路径
pule = os.path.split(r"c:\a\b\file.txt")  #分离文件和路径
print(pule[0])
print(os.path.dirname(r"c:\a"))  #取路径
print(os.path.basename(r"c:\a\b\file.txt")) #取文件

print(os.path.exists(r"c:\a\b\c"))
if os.path.exists(r"c:\a\b\c"):  #判断文件是否存在
    print("exit")
else:
    os.mkdir(r"c:\a\b\c")  #层级创建目录

os.chdir(r"c:\a\b")  #切换目录
print(os.path.isabs("file.txt"))  #  判断是否是绝对路径

print(os.path.isfile(r"c:\a\b\file.txt"))  #判断文件是否存在
print(os.path.isdir(r"c:\a\e"))  # 判断路径是否存在
print(os.path.join(r"c:",r"\a\b"))  #拼接路径
print(os.path.getatime(r"c:\a\b\file.txt"))   #获取文件atime
print(os.path.getmtime(r"c:\a\b\file.txt"))   #获取文件mtime




#  a/b/c
#  aos.sepbos.sep
#  print(a/b/c)  #linux,windows(err)
#  if os.system == linux
#     print(a/b/c)
#  if os.system == windows
#     print(a\b\c)
