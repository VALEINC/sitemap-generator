#hulu
from bs4 import BeautifulSoup
import requests
from datetime import date

hulu_unclean_urls = []
sitemap_list = ["https://www.hulu.com/sitemap/movies", "https://www.hulu.com/sitemap/series"]
num = 0
while num < len(sitemap_list):
	all_hulu = sitemap_list[num]
	response = requests.get(all_hulu)
	soup = BeautifulSoup(response.content, "html.parser")
	for link in soup.findAll('a'):
		if link.get('href') == None:
			pass
		else:
			hulu_unclean_urls.append(link.get('href'))
	num +=1
	continue
