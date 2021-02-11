import advertools
#import pandas
import dataframe

peacock_movies_sitemap = advertools.sitemap_to_df("https://www.peacocktv.com/sitemap-content_page_movies-0.xml")

for row in peacock_movies_sitemap['loc']:
    if "/seasons/" in row:
        print(row)
    else:
        pass

'''for (columnName, columnData) in peacock_movies_sitemap.iteritems():
   print('Colunm Name : ', columnName)
   print('Column Contents : ', columnData.values)'''