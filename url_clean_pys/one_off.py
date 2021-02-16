def appletv_clean(url):
    if "https://tv.apple.com/us/movie/" or "https://tv.apple.com/us/show/" in url:
        if "l=en" in url:
            url.strip("l=en")
            return url
        else:
            return url
    else:
        pass

def dazn_clean(url):
    if ("competitor" in url) or ("sport"  in url) or ("schedule" in url):
        pass
    elif 'https://www.dazn.com/en-US/home' == url:
        pass
    else:
        return url

def disneyplus_clean(url):
    if ("https://www.disneyplus.com/movies/" in url) or ("https://www.disneyplus.com/series/" in url):
		return url
	else:
		pass

def hbomax_clean(url):
    if ("https://www.hbomax.com/feature/urn" in url) or ("https://www.hbomax.com/series/urn" in url:):
        return url
    else:
        pass
    
def hulu_clean(url):

def netflix_clean(url):
    if "https://www.netflix.com/title/" in url:
        return url
    elif "%3A%2F%2F" in url:
        newurl = url.replace("https://www.netflix.com/login?nextpage=", "").replace("%3A", ":").replace("%2F", "/")
        return newurl
        #code to strip country code?
    else:
        pass
    
def peacock_clean(url):
	if ("/seasons/" in url) or ("/watch-online/") in url):
		return url
    else:
        pass