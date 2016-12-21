##Layer4Scraper
##Layer4ScraperException
##GeneralScraper

class GeneralScraper:
    '''
    This is a general scrapter class for layer 1,2,3
    type for the target layers are dicts
    '''
    def __init__(self, generalDict={}):
        self.resultSet = generalDict

    def listKeys(self):
        if(len(self.resultSet)>0):
            keyList = []
            for key in self.resultSet:
                keyList.append(key)
            return keyList
        else:
            raise Layer4ScraperException("This list is empty!")

    def addRecord(self, record):
        self.resultSet.append(record)

    

class Layer4ScraperException(Exception):
    def __init__(self, message, errors):
        super(ValidationError, self).__init__(message)
        self.errors = errors
    
class Layer4Scraper(GeneralScraper):
    '''
    This is Layer4Scraper Class
    type for the target layers are list
    Layer4 Contain a list of dict of all resturant information.
    '''
    def __init__(self, layer4List=[]):
        self.resultSet = layer4List

    def listKeys(self):
        if(len(self.resultSet)>0):
            keyList = []
            for key in self.resultSet[0]:
                keyList.append(key)
            return keyList
        else:
            raise Layer4ScraperException("This list is empty!")

    def outputFile():
        print("write later in Output file class")

    


    
    
