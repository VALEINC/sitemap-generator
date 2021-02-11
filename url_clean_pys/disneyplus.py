#Need to pull over fresh sitemap from disney before url_clean

#Do we need all of the various country designated titles? or will movies/series be enough

#open url output file

good_urls = []

for url in txtfile:
    if "https://www.disneyplus.com/movies/" or "https://www.disneyplus.com/series/" in url:
        good_urls.append(url)
    else:
        pass

#write urls to new outfile
