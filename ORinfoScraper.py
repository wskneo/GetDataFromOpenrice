# This is the main program, supposingly doing all the fetching job
# Open rice info scraper
import requests
from bs4 import BeautifulSoup
import json
from ScraperMethods import *

headersMobi = {'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Mobile Safari/537.36'}
openRiceApi = "https://www.openrice.com/api/pois?isnearby=true&uiLang=zh&uiCity=hongkong&page=1&&geo=22.280454199999998,114.1736493&sortBy=Default&withinDistance=0.5"


class OpenriceInfoScraper:
    def __init__(self,headersMobi,openRiceApi):
        self.headersMobi = headersMobi
        self.openRiceApi = openRiceApi
    


if __name__ == '__main__':
    try:

        r = requests.get(openRiceApi, headers=headersMobi)
        print("************key in 1 st layer")
        layer1Scraper = GeneralScraper(r.json())
        print("number of keys :", len(layer1Scraper.listKeys()))
##        print(layer1Scraper.listKeys())
        print("************key in 2 nd layer")
        layer2Scraper = GeneralScraper(layer1Scraper.resultSet["searchResult"])
        print("number of keys :", len(layer2Scraper.listKeys()))
        print("************key in 3 rd layer")
        layer3Scraper = GeneralScraper(layer2Scraper.resultSet["paginationResult"])
        print("number of keys :", len(layer3Scraper.listKeys()))  
        print("************4 th layer")
        layer4Scraper = Layer4Scraper(layer3Scraper.resultSet["results"])
        print("len of layer4Scraper :",len(layer4Scraper.resultSet))
        print("number of keys :", len(layer4Scraper.listKeys()))
    except Exception as e:
        print(e)
    finally:
        print("END")
