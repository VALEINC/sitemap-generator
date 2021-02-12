# peacocktv.py
import sys
from datetime import date
import logging
import requests
import xml.etree.ElementTree as ET
from pysitemap import crawler

if __name__ == '__main__':
	#peacock movies sitemap
	url_list = []
	xml_list = ["https://www.peacocktv.com/sitemap-content_page_entertainment-0.xml", "https://www.peacocktv.com/sitemap-content_page_entertainment-1.xml", "https://www.peacocktv.com/sitemap-content_page_entertainment-2.xml", "https://www.peacocktv.com/sitemap-content_page_news-0.xml"]
	num = 0
	xml_map = xml_list[num]
	while True:
		try:
			response = requests.get(xml_map)
			tree = ET.ElementTree(ET.fromstring(response.content))
			root = tree.getroot()
			for child in root:
				full_link = child[0].text
				series = full_link.split("/seasons/")[0]
				if series not in url_list:
					url_list.append(series)
			print("this keeps hitting, please quit out of meeeeeee")
			if num < len(api_list):
				num +=1
				continue
			else:
				print(url_list)
				break
'''response = requests.get('https://www.peacocktv.com/sitemap-content_page_entertainment-1.xml')
tree = ET.ElementTree(ET.fromstring(response.content))
root = tree.getroot()
for child in root:
	url_list.append(child[0].text)
list_urls = []
for i in url_list:
	series = i.split("/seasons/")[0]
	if series not in list_urls:
		list_urls.append(series)'''


#today=date.today()
#d=today.strftime("%m.%d.%y")
#with open(f'outputs/peacocktvseries-{d}.txt', "w") as outfile:       
#outfile.write('%s\n' % series)
#print(list_urls)
'''list_final = []
for url in list_urls:
	if url not in list_final:
		list_final.append(url)'''



#Other xml sitemap pages
#["https://www.peacocktv.com/sitemap-content_page_entertainment-0.xml", "https://www.peacocktv.com/sitemap-content_page_entertainment-1.xml", "https://www.peacocktv.com/sitemap-content_page_entertainment-2.xml", "https://www.peacocktv.com/sitemap-content_page_news-0.xml"]


### The method below works with most urls but there are always 3 urls raising errors 
# import sys
# from datetime import date
# import logging
# from .. import pysitemap

# if __name__ == '__main__':
#     if '--iocp' in sys.argv:
#         from asyncio import events, windows_events
#         sys.argv.remove('--iocp')
#         logging.info('using iocp')
#         el = windows_events.ProactorEventLoop()
#         events.set_event_loop(el)

#     # root_url = sys.argv[1]
#     root_url = 'https://www.peacocktv.com/'
#     today = date.today()
#     d = today.strftime("%m.%d.%y")
#     crawler(root_url, out_file=f'/Users/harperhe/Documents/Vale/Github/scrapy-tsg/urlgen/outputs/peacocktv{d}.txt', out_format='txt')
