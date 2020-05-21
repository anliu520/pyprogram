#Author:Anliu
from xml.etree import ElementTree as ET
tree = ET.parse("test_xml.xml")
url = tree.find("url")   #表示匹配到的第一个标签的内容
#it = tree.iter("url")    #标签的内容
#print(url.url)
#print(tree.iter(url).text
for key in tree.iter("url"):    #for循环->迭代器
    key.text = "http://www.souhu.com"
tree.write("test_xml.xml")