#Author:Anliu

#f1 = open("test1","w",encoding="utf-8")  #创建一个新文件，把旧文件覆盖
#f1 = open("test4","a",encoding="utf-8")  #当文件不存在时，创建；文件存在时，在文件后追加内容
#f1.write("康桥是今晚的沉默")
#f1 = open("test4","r+",encoding="utf-8")  #以读写的方式打开文件
#print(f1.read())
#f1.write("\n沉默是今晚的康桥")
#print(f1.read())
#f1.close()
#f1 = open("test4","a+",encoding="utf-8")  #追加读
#f1.write("\n沉默是今晚的康桥")
#f1.seek(0)
#print(f1.read())
#f1.close()
#f1 = open("test4","w+",encoding="utf-8")  #写读
#f1.write("\n沉默是今晚的康桥")
#f1.seek(0)
#print(f1.read())
#f1.close()
#"网络传输"，"视频文件"
f1 = open("test4","wb")  #二进制读
f2 = open("test4","rb")  #二进制写

