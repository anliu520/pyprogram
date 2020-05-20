#Author:Anliu
from xml.etree import ElementTree as ET
def build_sitemap():
    urlset = ET.Element("urlset")
    url = ET.SubElement(urlset,"url")
    loc = ET.SubElement(url,"url")
    loc.text = "http://www.baidu.com"
    lastmod = ET.SubElement(url,"lastmod")
    lastmod.text = "2020-5-20"
    changefreq = ET.SubElement(url,"changefreq")
    changefreq.text = "daily"


    tree = ET.ElementTree(urlset)
    tree.write("test_xml.xml")

if __name__ == '__main__':
    build_sitemap()

