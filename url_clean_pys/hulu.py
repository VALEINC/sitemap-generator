#open url output file

good_urls = []

for url in txtfile:
    if "https://www.hulu.com/series/" in url:
        if "referrer=sitemappage" in url:
            pass
        else:
            good_urls.append(url)
    elif "https://www.hulu.com/movie" in url:
        if "referrer=sitemappage" in url:
            pass
        else:
            good_urls.append(url)
    else:
        pass

#write urls to new outfile