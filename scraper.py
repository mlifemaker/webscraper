#! /usr/bin/python
#-*-coding:utf-8 -*-

from urllib2 import urlopen
from bs4 import BeautifulSoup
import nltk
import pickle
import jabba_webkit as jw
import re


url_base="http://www.skyscanner.fr/"
PatPrices=re.compile('<div class="mainquote-price big">(.*)</div>')
PatFlights=re.compile('<span data-carrier-ids=".*">(.*)</span>')
PatAirlines=re.compile('<div class="leg-airline">(.*)</div>')
PatFlightTime=re.compile('<div class="leg-flight-time">(.*)</div>')
PatCurrency=re.compile('<span class="curency-name">(.*)</span>')
#route=[fromaeroport,toaeroport,fromcity,tocity]
#date=[year,monthnumber, month,day]


def urlformatting(route, date):
	print url_base
	
	print date[0][2:]
	request_url=url_base+"transport/vols/"+route[0]+"/"+route[1]+"/"+date[0][2:]+date[1]+date[3]+"/"+"tarifs-de-"+route[2]+"-a-"+route[3]+"-en-"+date[2]+"-"+date[0]+".html?rtn=0"

	print request_url
	return request_url
	
def scrapAjaxWebpage(url):
	
	html=(jw.get_page(url)).encode('ascii','ignore')
	#results=re.findall(pattern, html)
	with open("dataAjax.txt","w") as ajaxdata:
		ajaxdata.write(html)
	#results=""
	#flights=[]
	#prices=[]
	#with open("dataAjax","r") as mydata:
		#results=mydata.read()
	prices=re.findall(PatPrices,html)
	#flights=re.findall(PatFlights,html)
	airlines=re.findall(PatAirlines,html)
	times=re.findall(PatFlightTime,html)
	departuretimes=[]
	arrivaltimes=[]
	for i in range(len(times)):
		if i%2==0:
			departuretimes.append(times[i])

		else:
			arrivaltimes.append(times[i])
	FlightResults={}
	
	for i in range(len(airlines)):
		FlightResults["flight"+str(i+1)]={}
		FlightResults["flight"+str(i+1)]["airline"]=nltk.clean_html(airlines[i])
		FlightResults["flight"+str(i+1)]["price"]=str(prices[i])+" EUR"
		FlightResults["flight"+str(i+1)]["departure time"]=departuretimes[i]
		FlightResults["flight"+str(i+1)]["arrival time"]=arrivaltimes[i]
		
	
	#print "airlines : %r prices: %s departure times: %s arrival times: % s" % (airlines, prices, departuretimes, arrivaltimes)
	print FlightResults
	with open("scrapedflightsprices.txt","w") as scrapeddata:
		mypickle=pickle.Pickler(scrapeddata)
		mypickle.dump(FlightResults)
		
	return FlightResults

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
	
	date=["2014","01","janvier","14"]
	route=["cdg","rba","paris","rabat"]
	urlreq=urlformatting(route, date)
	
	scrapajax=scrapAjaxWebpage(urlreq)
	#scrapit=scrap(depart, arrival)
	#data=extract_data(scrapit)
	#text=clean_text(url)
	#print data
	#print text 
