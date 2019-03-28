from bs4 import BeautifulSoup
import os
import requests
import time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import sys
import unicodecsv as csv

memelinks=[]

options=Options()
options.headless=True
firefox_profile=webdriver.FirefoxProfile()
firefox_profile.set_preference('permissions.default.image',2)
memesource=webdriver.Firefox(firefox_profile=firefox_profile,options=options)
memesource.get("https://knowyourmeme.com/memes/popular")

for i in range(100):
	memesource.execute_script("window.scrollTo(0, document.body.scrollHeight);")
	time.sleep(0.9)
content = memesource.page_source
memes = BeautifulSoup(content,features="lxml")
memesource.close()
memesource.quit()
urls=memes.find('tbody',{"class":"entry-grid-body infinite"}).find_all('a',{"class":"photo"})
print len(urls)

#individual meme parsing
for urlB in urls:
	url="https://knowyourmeme.com"+urlB['href']
	dire=url.split("/")[-1]
	try:
		os.makedirs(dire)
	except:
		   print 'next iteration'
		   continue
	options=Options()
	options.headless=True
	browser=webdriver.Firefox(options=options)
	browser.get(url)
	content = browser.page_source
	soup = BeautifulSoup(content,features="lxml")
	browser.close()
	browser.quit()
	#find pictures
	temp=soup.find('section',{"class":"bodycopy"}).find_all('center')
	imgs=[]
	for center in temp:
		pictures=center.find_all('img')
		for img in pictures:
			imgs.append(img)
	tocsv=[]
	for img in imgs:
		r = requests.get(img['data-src'], allow_redirects=True)
		open(dire+"/"+img['data-src'].split("/")[-1], 'wb').write(r.content)
		tocsv.append(img['data-src'].split("/")[-1])
	#find tags
	tagstocsv=[]
	
	tags=soup.find("dl", {"id": "entry_tags"}).find("dd").find_all('a')
	for element in tags:
		tagstocsv.append(element.string)
	with open(dire+"/"+dire+".csv", 'w') as csvFile:
	    writer = csv.writer(csvFile)
	    writer.writerow(tocsv)
	    writer.writerow(tagstocsv)
	csvFile.close()
	print dire

# if len(sys.argv)>1:
# 		url=sys.argv[1]
# 		print url
# 	else:
# 		print 'maybe try a link'