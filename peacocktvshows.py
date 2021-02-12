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
	xml_list = ["https://www.peacocktv.com/sitemap-content_page_movies-0.xml", "https://www.peacocktv.com/sitemap-content_page_entertainment-0.xml", "https://www.peacocktv.com/sitemap-content_page_entertainment-1.xml", "https://www.peacocktv.com/sitemap-content_page_entertainment-2.xml", "https://www.peacocktv.com/sitemap-content_page_news-0.xml"]
	print(len(xml_list))
	num = 0
	xml_map = xml_list[num]
	while True:
		try:
			xml_map = xml_list[num]
			print(xml_map)
			response = requests.get(xml_map)
			tree = ET.ElementTree(ET.fromstring(response.content))
			root = tree.getroot()
			for child in root:
				full_link = child[0].text
				if ("/seasons/") in full_link:
					pass
					#if we ever need to get the series link from the "seasons" url, see below:
						#series = full_link.split("/seasons/")[0]
				elif ("/watch-online/") in full_link:
					#print(full_link)
					url_list.append(full_link)
				else:
					pass
			num +=1
			if num < len(xml_list):
				continue
			else:
				print("you made it this far")
				today=date.today()
				d=today.strftime("%m.%d.%y")
				with open(f'outputs/peacocktv-{d}.txt', "w") as outfile:       
					outfile.write('%s\n' % url_list)
				break
		except:
			print("Something went wrong")
			break



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
