def appletv_clean(url):
	if "https://tv.apple.com/us/movie/" or "https://tv.apple.com/us/show/" in url:
		if "l=en" in url:
			url.strip("l=en")
			return url
		else:
			return url
	else:
		return None

def dazn_clean(url):
	if "/home/" in url:
		return url
	else:
		pass

def disneyplus_clean(url):
	if ("https://www.disneyplus.com/movies/" in url) or ("https://www.disneyplus.com/series/" in url):
		return url
	else:
		return None

def hbomax_clean(url):
	if ("https://www.hbomax.com/feature/urn" in url) or ("https://www.hbomax.com/series/urn" in url):
		return url
	else:
		return None
	
def hulu_clean(url):
	#code written to reflect sitemap links vs non-sitemap links
	if ('/movie/' in url) or ('/series/' in 'url'):
		if "?lp_referrer=sitemappage" in url:
			url.strip("?lp_referrer=sitemappage")
		if "https://www.hulu.com" in url:
			return url
		else:
			new_url = "https://www.hulu.com" + url
			return new_url
	else:
		return None

def netflix_clean(url):
	if "https://www.netflix.com/title/" in url:
		return url
	elif "%3A%2F%2F" in url:
		newurl = url.replace("https://www.netflix.com/login?nextpage=", "").replace("%3A", ":").replace("%2F", "/")
		return newurl
	else:
		return None

def peacock_clean(url):
	if "/seasons/" in url:
		return None
	elif "/watch-online/" in url:
		return url
	else:
		return None