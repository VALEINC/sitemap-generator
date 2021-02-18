# peacocktv.py
import requests
import xml.etree.ElementTree as ET

def peacock_sitemap():
	xml_list = ["https://www.peacocktv.com/sitemap-content_page_movies-0.xml", "https://www.peacocktv.com/sitemap-content_page_entertainment-0.xml", "https://www.peacocktv.com/sitemap-content_page_entertainment-1.xml", "https://www.peacocktv.com/sitemap-content_page_entertainment-2.xml", "https://www.peacocktv.com/sitemap-content_page_news-0.xml"]
	num = 0
	peacock_urls = []
	while num < len(xml_list):
		xml_map = xml_list[num]
		response = requests.get(xml_map)
		tree = ET.ElementTree(ET.fromstring(response.content))
		root = tree.getroot()
		for child in root:
			peacock_urls.append(child[0].text)
		num +=1
		continue
	return peacock_urls

if __name__ == '__main__':
	peacock_sitemap()