#dazn
import sys
from datetime import date
import logging
import requests
import xml.etree.ElementTree as ET
from pysitemap import crawler

if __name__ == '__main__':
    url_list = []
    response = requests.get('https://www.dazn.com/en-US/sitemap.xml')
    tree = ET.ElementTree(ET.fromstring(response.content))
    root = tree.getroot()
    for child in root:
        url_list.append(child[0].text)
    today=date.today()
    d=today.strftime("%m.%d.%y")
    with open(f'outputs/dazn{d}.txt', "w") as outfile:
        for i in url_list:
            if ("competition" in i) or ("/home/" in i) or ("ArticleId" in i):
                outfile.write('%s\n' % i)
            else:
                pass




# clean based on assumption that we don't want these types of urls ('https://www.dazn.com/en-US/competitor/Competitor:ipenlq6r1ae65q69twfd6ukr', 'https://www.dazn.com/en-US/sport/Sport:25z21evc6o0aewxnhyu2dzyrc', 'https://www.dazn.com/en-US/schedule')

'''BUCKET_NAME = 'tsguide'

            s3c = boto3.client(
                's3',
                region_name='us-east-1',
                aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
                aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY
            )

            response = s3c.put_object(
                Body=photo,
                Bucket=BUCKET_NAME,
                ContentType='image/jpeg',
                Key=f"images/users/{user.profile_picture_uid+connector+str(user.id)}.jpg"
            )'''