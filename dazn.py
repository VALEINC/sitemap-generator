#dazn
import sys
from datetime import date
import logging
import requests
import xml.etree.ElementTree as ET
from pysitemap import crawler

dazn_unclean_urls = []
response = requests.get('https://www.dazn.com/en-US/sitemap.xml')
tree = ET.ElementTree(ET.fromstring(response.content))
root = tree.getroot()
for child in root:
    dazn_unclean_urls.append(child[0].text)
