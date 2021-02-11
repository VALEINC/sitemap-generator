#disneyplus.py
import sys
from datetime import date
import logging
import requests
import xml.etree.ElementTree as ET
import pysitemap
from pysitemap import crawler

if __name__ == '__main__':

    url_list = []

    tree = ET.parse('local_sitemaps/d-sitemap-1.xml')
    root = tree.getroot()

    for child in root:
        url_list.append(child[0].text)

    today=date.today()
    d=today.strftime("%m.%d.%y")
    with open(f'outputs/disneyplus{d}.txt', "w") as outfile:
        for i in url_list:
            outfile.write('%s\n' % i)
