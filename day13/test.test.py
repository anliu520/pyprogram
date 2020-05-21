#Author:Anliu
import xml.etree.ElementTree as ET
tree = ET.parse("test.xml")
root = tree.getroot()
#print(root.findall("country"))   #查找所有
for i in root.findall("country"):
    #print(i.find("gdppc").text)
    if int(i.find("gdppc").text) > 100000:
        for k in i:
            #print(k.tag,k.text)
            #print(k.tag)
            if k.tag == "gdppc":
                print(k.tag)
                i.remove(k)
    #print(i.tag)
    #print(type(i.find("rank").text))
    #if int(i.find("rank").text) > 50:
    #    root.remove(i)
    #print(i.tag)
tree.write("test.xml")