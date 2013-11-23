#-*-coding:utf-8 -*-

from urllib2 import urlopen
from bs4 import BeautifulSoup

def scrap(url):
	html=urlopen(url).read()
	soup=BeautifulSoup(html,"lxml")
	#context=soup.get_text()
	return soup


def extract_data(soup):

	data=soup.get_text()
	return data 




if __name__=="__main__":

	url="http://www.royalairmaroc.com"
	scrapit=scrap(url)
	data=extract_data(scrapit)
	print data
