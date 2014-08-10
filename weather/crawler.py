__author__ = 'luosha865'
import urllib2
from bs4 import BeautifulSoup

USCitys=[]

class Crawler:
    url = ""
    soup = None
    def __int__(self):
        pass
    def ReadPage(self,url):
        page = urllib2.urlopen(url)
        self.url = url
        self.soup = BeautifulSoup(page)
    def ReadCityHistoryWeather(self,city,year,month,day):
        url ="http://www.wunderground.com/history/airport/%s/%d/%d/%d/DailyHistory.html"%(city,year,month,day)
        print url
        self.ReadPage(url)
    def getPrecipitation(self):
        if self.soup==None:
            return
        wx =weathercrawler.soup.findAll(attrs={"class":"wx-value"})
        precipitation =  wx[10].string
        if precipitation == 'T':
            precipitation = 0
        return float(precipitation)
    def getHistoryAvgPrecipitation(self):
        if self.soup==None:
            return
        wx =weathercrawler.soup.findAll(attrs={"class":"wx-value"})
        precipitation =  wx[11].string
        if precipitation == 'T':
            precipitation = 0
        return float(precipitation)


weathercrawler = Crawler()
#weathercrawler.ReadPage("http://www.wunderground.com/history/airport/KBUF/2009/1/1/DailyHistory.html")
weathercrawler.ReadCityHistoryWeather("KBUF",2009,1,1)
