#open url output file

good_urls = []

for url in txtfile:
    if "https://www.hbomax.com/feature/urn" in url:
        good_urls.append(url)
    elif "https://www.hbomax.com/series/urn" in url:
        good_urls.append(url)
    else:
        pass

#write urls to new outfile

#possibly helpful?
    #"coming-soon" urls
    #"watch-free" urls
