# from beautifulsoup4 import beautifulsoup4
# import urllib2

# response = urllib2.urlopen('http://en.wikipedia.org/wiki/Python_(programming_language)')
# html = response.read()
 
# parsed_html = BeautifulSoup(html)
# 
# ------------------------------------------------------

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


# ------------------------------------------------------

# from bs4 import BeautifulSoup
# import time
# from selenium import webdriver

# url = "https://www.basketball-reference.com/leagues/NBA_2017_standings.html"
# browser = webdriver.Firefox()

# browser.get(url)
# time.sleep(3)
# html = browser.page_source
# soup = BeautifulSoup(html, "lxml")

# print(len(soup.find_all("table")))
# print(soup.find("table", {"id": "expanded_standings"}))

# browser.close()
# browser.quit()