from bs4 import BeautifulSoup
# import urllib2
import time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import sys
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
for img in imgs:
	print img['data-src']

#find tags
print 'TAGS BRO:'
tags=soup.find("dl", {"id": "entry_tags"}).find("dd").find_all('a')
for element in tags:
	print element.string