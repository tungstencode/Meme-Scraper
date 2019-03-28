from bs4 import BeautifulSoup
import os
import requests
import time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import sys
import unicodecsv as csv
#happens once
options=Options()
options.headless=True
firefox_profile=webdriver.FirefoxProfile()
firefox_profile.set_preference('permissions.default.image',2)
memesource=webdriver.Firefox(firefox_profile=firefox_profile,options=options)
memesource.get("https://knowyourmeme.com/memes/popular")

# optimized
#fac asta de 10 ori
for k in range(2):
	# scot html din 10 falea
	for i in range(5):
		memesource.execute_script("window.scrollTo(0, document.body.scrollHeight);")
		time.sleep(random.uniform(1,3))
	content = memesource.page_source
	memes = BeautifulSoup(content,features="lxml")
	urls=memes.find('tbody',{"class":"entry-grid-body infinite"}).find_all('a',{"class":"photo"})
	print 'getting html for the '+k+' time'
	# rulez alea 10 prin downloader
	for urlB in urls:
		url="https://knowyourmeme.com"+urlB['href']
		dire=url.split("/")[-1]
		try:
			os.makedirs(dire)
		except:
			   print 'we have '+dire+' already, next meme'
			   continue
		browser=webdriver.Firefox(firefox_profile=firefox_profile,options=options)
		browser.get(url)
		content = browser.page_source
		soup = BeautifulSoup(content,features="lxml")
		print 'getting data from '+url
		browser.close()
		browser.quit()
		print 'killed '+url+', now filtering.'
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
		print dire+' meme was saved.'
		time.sleep(random.uniform(1,3))
	#mai scot 10 dalea

memesource.close()
memesource.quit()





















