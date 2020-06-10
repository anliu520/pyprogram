#Author:Anliu
import re
#(1)compile()  生成正则对象

#reg = re.compile("^Cheng")   #生成正则对象
#print(reg)
#print(reg.match("Chengxierun"))

#（2）group()  获取匹配到的值
#print(reg.match("Chengxierun").group())    #group() 获取匹配到的值
#reg = re.match("^cheng","Chengxuerun")
#print(reg)
#print(reg.group())

#(3)search() 匹配复合条件的所有内容
#print(re.search("\w+","abcde").group())   #search() 匹配复合条件的所有内容
#print(re.search("a","bcdea").group())

#(4)#match（） 匹配第一个匹配的内容。
#print(re.match("\w","abcdf").group())    #match（） 匹配第一个匹配的内容。
#print(re.match("a","bcdea"))

#print(re.search('a','absabc').group())
#print(re.match('a','bsabca'))
#
#print(re.search('\D+','abc123com').group())  #非数字
#print(re.match('\D+','123comabc').group())
#
#rint(re.search('\d+','abc123com').group())
#print(re.match('\d+','abc123com').group())  #match报错

#(5) fullmatch() 匹配所有内容
#print(re.fullmatch("abb","abb123"))
#print(re.fullmatch('\w+',"abc123").group())

#(6) split() 分割
#print(re.split("[a,b]","123a4b56a789"))
#print(re.split(r'\W+','Words,words,words.'))
#print(re.split(r'(\W+)','Words,words,words.'))
#print(re.split('[a-f]+','0a3B9',flags=re.IGNORECASE))  #flags=re.IGNORECASE 在匹配时不区分大小写。

#（7）findall() 把匹配到的内容以列表的形式呈现，从左到右。
print(re.findall("\d+","123a4b56a789"))

#(8) finditer() 生成的是迭代器对象。
#
#print(re.finditer("[a]","This is am a apple...."))
#reg = re.finditer("[a,s]","This is am a apple....")
#print(reg.__next__())
#print(reg.__next__())
#print(reg.__next__())
#print(reg.__next__())
#for i in reg:
#    print(i.group())

#(9)sub 替换,以字符串的形式展示
#print(re.sub("\d+","...","123abc456deh789bbb",4))

#（10）subn 替换，以元组的形式展示
#print(re.subn("\d+","...","123abc456deh789bbb",2))

#(11) escape()  转义
#print(re.escape("http://www.baidu.com"))
#print(re.findall(re.escape("http:\\"),"http:\\www.http.com"))


#line = "http://www.python.py"
#pat = "(?<=\.).+(?=\.)"
#patobj = re.compile(pat)

# 应用正则两种方式：
#（1）调re方法串参数
#（2）用对象调方法
#print(patobj.search(line).group())
#print(re.search(pat,line).group())
#print(re.search(patobj,line).group())
#print(patobj.sub('java',line))
#print(re.sub(patobj,'java1',line))
#print(re.sub(pat,"java2",line))

line1 = "http://www.baidu.com"
line2 = "ftp://www.baidu.com"

pat = "^http.*"
patobj = re.compile(pat)
print(patobj.search(line1).group())
print(patobj.search(line2))

