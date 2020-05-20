#Author:Anliu
import xml.etree.cElementTree as ET
tree = ET.parse("centos7.xml")
root = tree.getroot()
#print(root.tag)
#print(root.text)

#for child in root:
#    print(child.tag,child.text,child.attrib)
#    for i in child:
#        print(i.tag,i.text)
for node in root.iter("name"):
    print(node.tag,node.text)
    node.text = "hahaha"
    print(node.tag,node.text)
tree.write("centos7.xml")