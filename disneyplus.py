#disneyplus
import requests
import xml.etree.ElementTree as ET

def disney_sitemap():
	disney_urls = []
	response = requests.get('https://cde-lumiere-disneyplus.bamgrid.com/d-sitemap-1.xml')
	tree = ET.ElementTree(ET.fromstring(response.content))
	root = tree.getroot()
	for child in root:
		disney_urls.append(child[0].text)
	return disney_urls

if __name__ == '__main__':
	disney_sitemap()