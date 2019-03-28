from bs4 import BeautifulSoup
import os
import requests
import time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import sys
import csv
url = "https://knowyourmeme.com/memes/trollface"
if len(sys.argv)>1:
	url=sys.argv[1]
	print url
else:
	print 'maybe try a link'
options=Options()
options.headless=True
browser=webdriver.Firefox(options=options)
browser.get(url)
content = browser.page_source
soup = BeautifulSoup(content,features="lxml")
browser.close()
browser.quit()
#find pictures
print 'PICTURES BRO:'
temp=soup.find('section',{"class":"bodycopy"}).find_all('center')
imgs=[]
for center in temp:
	pictures=center.find_all('img')
	for img in pictures:
		imgs.append(img)
dire=url.split("/")[-1]
tocsv=[]
try:
	os.makedirs(dire)
except OSError:
    print 'folder already made'
for img in imgs:
	r = requests.get(img['data-src'], allow_redirects=True)
	open(dire+"/"+img['data-src'].split("/")[-1], 'wb').write(r.content)
	tocsv.append(img['data-src'].split("/")[-1])



#find tags
tagstocsv=[]
print 'TAGS BRO:'
tags=soup.find("dl", {"id": "entry_tags"}).find("dd").find_all('a')
for element in tags:
	print element.string
	tagstocsv.append(element.string)


with open(dire+"/"+dire+".csv", 'w') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerow(tocsv)
    writer.writerow(tagstocsv)
csvFile.close()