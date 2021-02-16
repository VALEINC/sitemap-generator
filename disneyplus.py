#disneyplus
import sys
from datetime import date
import logging
import requests
import xml.etree.ElementTree as ET
from pysitemap import crawler

if __name__ == '__main__':
	url_list = []
	response = requests.get('https://cde-lumiere-disneyplus.bamgrid.com/d-sitemap-1.xml')
	tree = ET.ElementTree(ET.fromstring(response.content))
	root = tree.getroot()
	for child in root:
		url_list.append(child[0].text)
	today=date.today()
	d=today.strftime("%m.%d.%y")
	with open(f'outputs/disneyplus{d}.txt', "w") as outfile:
		for i in url_list:
			if "https://www.disneyplus.com/movies/" in i:
				outfile.write('%s\n' % i)
			elif "https://www.disneyplus.com/series/" in i:
				outfile.write('%s\n' % i)
			else:
				pass

# outfile is filled with good links only
# code to cross reference db now?