#-*-coding:utf-8 -*-

from urllib2 import urlopen
from bs4 import BeautifulSoup
import nltk

def scrap(url):
	html=urlopen(url).read()
	soup=BeautifulSoup(html,"lxml")
	#context=soup.get_text()
	return soup

def clean_text(url):
	html=urlopen(url).read()
	text=nltk.clean_html(html)
	return text

def extract_data(soup):

	data=soup.get_text()
	return data 




if __name__=="__main__":

	url="http://www.royalairmaroc.com"
	scrapit=scrap(url)
	data=extract_data(scrapit)
	text=clean_text(url)
	#print data
	print text 
