#open url output file

good_urls = []

for url in txtfile:
    if "https://www.netflix.com/title/" in url:
        good_urls.append(url)
    elif "%3A%2F%2F" in url:
        newurl = url.replace("https://www.netflix.com/login?nextpage=", "").replace("%3A", ":").replace("%2F", "/")
        good_urls.append(newurl)
    else:
        pass

#write urls to new outfile


 # Extra notes
     # contains "genre" -> pass
     # contains "browse" -> pass
     # "/watch/" -> free content. Useful?

     #Different Country Urls
         #Necessary? Unclear
         # "ca/title" -> strip ca
             # https://www.netflix.com/ca/title/81047664
         # "de-en/title" -> strip de-en
             # https://www.netflix.com/de-en/title/80073486
         # "ro-en/title" -> strip ro-en
             # https://www.netflix.com/ro-en/title/80067618
         # "sc/title" -> strip sc
             # https://www.netflix.com/sc/title/81084225
         # others?
