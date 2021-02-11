#Need to pull over fresh sitemap from disney before url_clean

#Do we need all of the various country designated titles? or will movies/series be enough

import advertools
#import pandas
#import dataframe

disney_sitemap = advertools.sitemap_to_df("https://cde-lumiere-disneyplus.bamgrid.com/d-sitemap-1.xml")
for row in disney_sitemap['loc']:
	good_urls = []
	if "https://www.disneyplus.com/movies/" in row:
		good_urls = good_urls.append(row)
		print(row)
	elif "https://www.disneyplus.com/series/" in row:
		good_urls = good_urls.append(row)
		print(row)
	else:
		pass
print(good_urls)



'''good_urls = []

for url in txtfile:
    if "https://www.disneyplus.com/movies/" or "https://www.disneyplus.com/series/" in url:
        good_urls.append(url)
    else:
        pass'''

#write urls to new outfile
