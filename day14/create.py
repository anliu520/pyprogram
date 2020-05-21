#Author:Anliu
#Author:Anliu
from xml.etree import ElementTree as ET
def build_sitemap():
    urlset = ET.Element("urlset")   #设置一个根节点，标签为urlset
    url = ET.SubElement(urlset,"url")
    loc = ET.SubElement(url,"loc")   #在根节点urlset下建立子节点
    loc.text = "http://www/baidu.com"
    lastmod = ET.SubElement(url,"lastmod")
    lastmod.text = "2020-4-13"
    changefreq = ET.SubElement(url,"changefreq")
    changefreq.text = "daily"
    priority = ET.SubElement(url,"priority")
    priority.text = "1.0"
    tree = ET.ElementTree(urlset)
    tree.write("test_xml.xml")
if __name__ == '__main__':
    build_sitemap()
