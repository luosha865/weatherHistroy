__author__ = 'luosha865'
import urllib2
from bs4 import BeautifulSoup
import requests
import json
import scrapy

USCitys=[]

class Crawler(object):
    url = ""
    soup = None
    def __int__(self):
        pass
    def ReadPage(self,url):
        response = requests.get(url)
        self.url = url
        self.hxs = scrapy.Selector(text = response.content)
        self.getPrecipitation()

    def ReadCityHistoryWeather(self,city,year,month,day):
        url ="http://www.wunderground.com/history/airport/%s/%d/%d/%d/DailyHistory.html"%(city,year,month,day)
        print url
        self.ReadPage(url)

    def getPrecipitation(self):
        if self.hxs==None:
            return
        self.precipitationlst = self.hxs.xpath("//td/span[text()='Precipitation']/parent::*/following-sibling::*//span[@class='wx-value']//text()").extract()

    def getHistoryAvgPrecipitation(self):
        if self.precipitationlst == None:
            return None
        precipitation =  self.precipitationlst[1]
        if precipitation == 'T':
            precipitation = 0
        return float(precipitation)


weathercrawler = Crawler()
#weathercrawler.ReadPage("http://www.wunderground.com/history/airport/KBUF/2009/1/1/DailyHistory.html")
weathercrawler.ReadCityHistoryWeather("KBUF",2009,1,1)
avgPrecipitation = weathercrawler.getHistoryAvgPrecipitation()
print avgPrecipitation