#hulu
from bs4 import BeautifulSoup
import requests
from datetime import date

url_list = []
sitemap_list = ["https://www.hulu.com/sitemap/movies", "https://www.hulu.com/sitemap/series"]
num = 0
while True:
	try:
		all_hulu = sitemap_list[num]
		response = requests.get(all_hulu)
		soup = BeautifulSoup(response.content, "html.parser")
		for link in soup.findAll('a'):
			if link.get('href') == None:
				pass
			elif ('/movie/' in link.get('href')) or ('/series/' in link.get('href')):
				new_link = ("https://www.hulu.com" + (link.get('href'))).strip("?lp_referrer=sitemappage")
				url_list.append(new_link)
			else:
				pass
		num +=1
		print(num)
		if num < len(sitemap_list):
			continue
		else:
			print("here, at least")
			today=date.today()
			d=today.strftime("%m.%d.%y")
			with open(f'outputs/hulu{d}.txt', "w") as outfile:
				outfile.write('%s\n' % url_list)
			break
	except:
		print("broken")
		break


'''for link in soup.findAll('a'):
	all_urls.append(link.get('href'))
for i in all_urls:
	if i == None:
		pass
	elif '/movie/' in i:
		new_link = ("https://www.hulu.com" + i).strip("?lp_referrer=sitemappage")
		#good_urls.append(new_link)
		print(new_link)
	else:
		pass
print(good_urls)'''


'''import sys
from datetime import date
import logging
import requests
import xml.etree.ElementTree as ET
from pysitemap import crawler
if __name__ == '__main__':
	url_list = []
	response = requests.get('https://www.hulu.com/sitemap/movies')
	tree = ET.ElementTree(ET.fromstring(response.content))
	root = tree.getroot()
	for child in root:
		url_list.append(child[0].text)
	print(url_list)
	today=date.today()
	d=today.strftime("%m.%d.%y")'''
	
'''with open(f'outputs/hulumovies{d}.txt', "w") as outfile:
	for i in url_list:
		if "https://www.disneyplus.com/movies/" in i:
			outfile.write('%s\n' % i)
		elif "https://www.disneyplus.com/series/" in i:
			outfile.write('%s\n' % i)
		else:
			pass'''



#neflix.py
'''import sys
from datetime import date
import logging
from .. import pysitemap

if __name__ == '__main__':
	if '--iocp' in sys.argv:
		from asyncio import events, windows_events
		sys.argv.remove('--iocp')
		logging.info('using iocp')
		el = windows_events.ProactorEventLoop()
		events.set_event_loop(el)

	# root_url = sys.argv[1]
	root_url = 'https://www.hulu.com/'
	today = date.today()
	d = today.strftime("%m.%d.%y")
	crawler(root_url, out_file=f'../outputs/hulu{d}.txt', out_format='txt')'''
	  