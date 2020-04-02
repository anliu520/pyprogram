#Author:Anliu

#a = "we love python"
#b = 123

#print(a,type(a))
#print(a[0:2])   # 字符串切片，“取头不取尾”
#print(a[1:])
#print(a[-4:-2])   #  “取头不取尾”
#print(a[2:6:2])   #  ::2  步长
#print(a[-6:-1:2])
#print(a*2)
#print(a + str(b))
#n = 0
#for i in a:
#    if i == "o":
#        n+=1
#else:
#    print(n)
b = "linuxs"
a = "{name} \tlove python,{ages}"
print(a.count("n"))
print(b.center(12,"+"))
print(a.capitalize())
print(a.encode())
print(a)
print(a.expandtabs(tabsize=3))  #"2"
print(a.endswith("python"))
print(a.format(name ="dongyu",ages = "18"))
dict = {"name":"runrun","ages":"16"}
print(a.format_map(dict))
c = "Linux Is A System"
print(c.find("x"))
print(type(c))
print(c.isdigit())
#print(c.index("x"))
print(c.istitle())
print(" ".isspace())
print("qqq".isprintable())  # 设备文件，终端（tty）文件
print("AAAA".islower())
print("and".isidentifier())  #判断是不是合法的标识符
print("1A".isdecimal())  #判断十进制
print("abc13e".isalpha())
print("abc_12e".isalnum())
print("1101".isnumeric())
a1 = "abc"
a2 = "efg"
print(a2.join(a1))
print("abc".ljust(4,"="))
print("        mckdsnclsdnv      ".rstrip())
print("        mckdsnclsdnv      ".lstrip())
print("        mckdsnclsdnv      ".strip())
p = str.maketrans("abcdefg","1234567")
print("abfg".translate(p))
print("nckjsq11".upper())
print("dads".zfill(30))
print("ad".replace("a","A"))
print("abcdefab".rsplit("b"))
print("baidu.com".startswith("www"))
print("we\nlive\nlinux ".splitlines())
print("ABC".swapcase())


