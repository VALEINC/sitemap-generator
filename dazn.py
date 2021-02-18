#dazn
import requests
import xml.etree.ElementTree as ET

def dazn_sitemap():
    dazn_urls = []
    response = requests.get('https://www.dazn.com/en-US/sitemap.xml')
    tree = ET.ElementTree(ET.fromstring(response.content))
    root = tree.getroot()
    for child in root:
        dazn_urls.append(child[0].text)
    return dazn_urls

if __name__ == '__main__':
	dazn_sitemap()