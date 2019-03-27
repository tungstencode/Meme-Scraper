from bs4 import BeautifulSoup
# import urllib2
import time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
url = "https://9gag.com"

options=Options()
options.headless=True
browser=webdriver.Firefox(options=options)
browser.get(url)
# browser.setJavascriptEnabled(true)
# browser.set_window_position(0, 0)
for i in range(3):
	browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
	time.sleep(0.05)

content = browser.page_source

soup = BeautifulSoup(content,features="lxml")
# print soup.prettify()
pictures=soup.find_all('picture')
print pictures
print pictures.pop().find('img')['src']
# print dir(pictures)
browser.close()
browser.quit()