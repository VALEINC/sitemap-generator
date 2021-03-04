from datetime import date
from platform_gens import *
from dazn import dazn_sitemap
from cleaners import *
from hulu import hulu_sitemap
import boto3
import os

def main():
	streaming_platforms = ["dazn", "hulu"]
	streaming_functions = [dazn_sitemap(), hulu_sitemap()]
	#streaming_functions = [appletv_sitemap(), dazn_sitemap(), disneyplus_sitemap(), hbomax_sitemap(), hulu_sitemap(), peacocktv_sitemap()]
	
	#streaming_platforms = ["appletv", "dazn", "disneyplus", "hbomax", "hulu", "peacocktv"]
	
	#add netflix ^ once it can finish
	num = 0
	while num < len(streaming_platforms):
		current_platform = streaming_platforms[num]
		current_function = streaming_functions[num]
		#url_list = f"{current_platform}_sitemap()"
		#url_list = dazn_sitemap()
		today = date.today()
		d = today.strftime("%m.%d.%y")
		with open(f'{current_platform}.{d}.csv', "w", encoding='utf-8') as outfile:
			for url in current_function:
				cleaning_functions = [dazn_clean(url), hulu_clean(url)]
				current_cleaner = cleaning_functions[num]
				url = current_cleaner
				if url == None:
					pass
				else:
					outfile.write('%s\n' % url)
		num+=1
		continue
'''
			BUCKET_NAME = 'tsguide'

			s3c = boto3.client(
				's3',
				region_name='us-east-1',
				aws_access_key_id = os.environ.get('ACCESS_KEY_ID'),
				aws_secret_access_key = os.environ.get('SECRET_ACCESS_KEY')
			)

			response = s3c.put_object(
				Body=outfile,
				Bucket=BUCKET_NAME,
				ContentType='text/csv',
				Key=f"scraping_files/{current_platform}.{d}.csv"     
			)
		num+=1
		continue	
'''
if __name__ == '__main__':
	main()

	'''final_urls = []
	for i in url_list:
		final_urls.append(f"{current_platform}_clean(i)")'''
	#make text file from final_urls
	#upload to s3 with some kind of standard name and date convetion

	#today = date.today()
	#d = today.strftime("%m.%d.%y")


'''
Body=photo,
Bucket=BUCKET_NAME,
ContentType='image/jpeg',
Key=f"images/users/{user.profile_picture_uid+connector+str(user.id)}.jpg"
'''