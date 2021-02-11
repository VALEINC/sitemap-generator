#open url output file

good_urls = []

for url in txtfile:
    if "l=en" in url:
        pass
    elif "https://tv.apple.com/us/movie/" or "https://tv.apple.com/us/show/" in url:
        good_urls.append(url)
    else:
        pass

#write urls to new outfile



#Now
    #movies "https://tv.apple.com/us/movie/"
        #remove (duplicate) movies with "?l=en"
    #shows "https://tv.apple.com/us/show/"
        #remove duplicate shows with "?l=en"

#Later
    #person "https://tv.apple.com/us/person/"
        #once we want people, remove (duplicate) people with: "?l=en"
    #episode "https://tv.apple.com/us/episode/
        #once we want episodes, remove (duplicate) titles with: "&amp;l=en"