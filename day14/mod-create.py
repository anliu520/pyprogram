#Author:Anliu
import xml.etree.cElementTree as ET


#tree = ET.parse("test_xml.xml")
#root = tree.getroot()
#url = tree.find("url")  #find,findall只能在当前标签下查找子标签，并返回子标签的存储对象
#loc = url.find("loc")   #可对子标签再次find

#print(url.find("loc"))  #打印子标签的存储对象
#print(root.tag,root.text)
#print(loc.tag)   #打印子标签名

#遍历：
#for en in tree.getroot():
#    print(en)   #打印根节点存储对象
#    for suben in en:
#        print(suben)  #打印子节点存储对象

#修改
tree1 = ET.parse("test1_xml.xml")
#root1 = tree1.getroot()
for en in tree1.getroot():  #遍历根节点标签
    print(en)   #打印根节点下的子节点存储对象
    print(en.tag)  #打印更节点下子节点的标签名
    for suben in en:  #遍历字节下的标签
        #print(suben.tag)
        if suben.tag == "url":
            suben.text = "www.xxxx.com"
        #print(suben)  #打印子节点存储对象
tree1.write("test1_xml.xml")