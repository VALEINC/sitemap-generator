#open url output file


import advertools
#import pandas
import dataframe

hulu_movies_sitemap = advertools.sitemap_to_df("https://www.hulu.com/sitemap/movies")
hulu_movies_sitemap
'''for (columnName, columnData) in hulu_movies_sitemap.iteritems():
   print('Colunm Name : ', columnName)
   print('Column Contents : ', columnData.values)'''

'''good_urls = []

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
        pass'''

#write urls to new outfile