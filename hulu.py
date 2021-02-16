#hulu
from bs4 import BeautifulSoup
import requests
from datetime import date

url_list = []
sitemap_list = ["https://www.hulu.com/sitemap/movies", "https://www.hulu.com/sitemap/series"]
num = 0
today=date.today()
d=today.strftime("%m.%d.%y")
with open(f'outputs/hulu{d}.txt', "w") as outfile:
	while num < len(sitemap_list):
		all_hulu = sitemap_list[num]
		response = requests.get(all_hulu)
		soup = BeautifulSoup(response.content, "html.parser")
		for link in soup.findAll('a'):
			if link.get('href') == None:
				pass
			elif ('/movie/' in link.get('href')) or ('/series/' in link.get('href')):
				new_link = ("https://www.hulu.com" + (link.get('href'))).strip("?lp_referrer=sitemappage")
				outfile.write('%s\n' % new_link)
			else:
				pass
		num +=1
		continue