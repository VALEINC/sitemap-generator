#disneyplus
import requests
import xml.etree.ElementTree as ET

disney_unclean_urls = []
response = requests.get('https://cde-lumiere-disneyplus.bamgrid.com/d-sitemap-1.xml')
tree = ET.ElementTree(ET.fromstring(response.content))
root = tree.getroot()
for child in root:
	disney_unclean_urls.append(child[0].text)
