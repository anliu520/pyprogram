#Author:Anliu

import xml.etree.ElementTree as ET
tree = ET.parse("centos7.xml")
#print(tree.getroot())
#for i in tree.getroot():
#    print(i.text,i.tag)
root = tree.getroot()
for node in root.iter("vcpu"):
    print(node.text)
#    new = int(node.text) + 1
    node.text = "5"
    node.set("updated","yes")

tree.write("centos7.xml")