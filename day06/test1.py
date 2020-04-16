#Author:Anliu
#-*- coding:gbk -*- _
import sys
print(sys.getdefaultencoding())
msg = "我们都是好孩子"
print(msg)
s_to_gbk = msg.encode("gbk").decode("gbk")
s_to_utf8 = msg.encode("utf8").decode("utf8")
s_to_gb2312 = msg.encode("gb2312").decode("gb2312")
print(s_to_gbk)
print(s_to_utf8)
print(s_to_gb2312)