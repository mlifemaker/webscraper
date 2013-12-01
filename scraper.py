#! /usr/bin/python
#-*-coding:utf-8 -*-

from urllib2 import urlopen
from bs4 import BeautifulSoup
import nltk
import pickle
import jabba_webkit as jw

url_base="http://skyscanner.fr/"

def scrapAjaxWebpage(url):
	
	html=(jw.get_page(url)).encode('ascii','ignore')
	with open("dataAjax.txt","w") as ajaxdata:
		ajaxdata.write(html)
	print html
	return html
def scrap(depart,arrival):
	url=url_base+"transport/vols/"+depart+"/"+arrival+"/"
	print(url)
	html=urlopen(url).read()
	soup=BeautifulSoup(html,"lxml")
	context=nltk.clean_html(html)
	with open("data.txt","w") as scraped_data:
		mydata=scraped_data.write(url)
	print(context)        		
	return soup

def clean_text(url):
	html=urlopen(url).read()
	text=nltk.clean_html(html)
	return text

def extract_data(soup):

		data=soup.get_text()
		return data 


	


if __name__=="__main__":
        url="http://www.skyscanner.fr/transport/vols/brus/casa/131214/tarifs-de-bruxelles-a-casablanca-en-decembre-2013.html?rtn=0"	
	url1="http://www.skyscanner.net"
	depart="cdg"
	arrival="casa"
	scrapajax=scrapAjaxWebpage(url)
	#scrapit=scrap(depart, arrival)
	#data=extract_data(scrapit)
	#text=clean_text(url)
	#print data
	#print text 
