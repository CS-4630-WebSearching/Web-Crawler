import scrapy
from bs4 import BeautifulSoup
from scrapy.http import Request
from urllib.request import urlopen
from englishScraper import English_Spider
import os

class StartSpider(scrapy.Spider):

    #name of the spider
    name = "start_Spider"
    #where spider will start crawling
    start_urls = ['https://www.cnn.com/2020/03/02/politics/hillary-clinton-emails-deposition/index.html']

    #get urls based on selectors
    def parse(self, response):
        #create a file in current directory
        outF = open("htmlData.txt", "w")
        #gets content inside the div tag with class name cd__content
        urlContent = response.xpath('//body//div/text()').extract()
        urlContentTwo = response.xpath('//body//div//p/text()').extract()
        urlContentThree = response.xpath('//body//p/text()').extract()
       
        print(urlContentTwo)
        outF.write(''.join(urlContentTwo))
        outF.write(''.join(urlContent))
        outF.write(''.join(urlContentThree))

'''
        for text in urlContent:
            par = text.xpath('./text()').extract_first()
            if par is not None:
                outF.write(par)
                print(par)
        outF.close()
        '''


   


        # #gets urls directly from the html file
        # for urls in urlContent:
        #     #takes a single url from list of urls
        #     url = urls.xpath('.//a/@href').extract_first()
        #     fixedURL = response.urljoin(url[0:])
 
        #     print(fixedURL


#create the file for storing parsed html text
def storenew_html(text, fileName):
    #combine filepath name with newly created file
    filepath = os.path.join('/Users/Bluck/Documents/Python Projects/searchEngine/searchEngine/spiders/parsed html docs', (str(fileName) + ".txt"))
    #checks if the directory exists
    if not os.path.exists('/Users/Bluck/Documents/Python Projects/searchEngine/searchEngine/spiders/parsed html docs'):
         #if directory does not exist then create it
        os.makedirs('/Users/Bluck/Documents/Python Projects/searchEngine/searchEngine/spiders/parsed html docs')
    #create the file    
    parsedFile = open(filepath, "w")
    parsedFile.write(text)
    parsedFile.close()

#append to the file for storing parsed html text
def append_html(text, fileName):
    #combine filepath name with newly created file
    filepath = os.path.join('/Users/Bluck/Documents/Python Projects/searchEngine/searchEngine/spiders/parsed html docs', (str(fileName) + ".txt"))
    #checks if the directory exists
    if not os.path.exists('/Users/Bluck/Documents/Python Projects/searchEngine/searchEngine/spiders/parsed html docs'):
         #if directory does not exist then create it
        os.makedirs('/Users/Bluck/Documents/Python Projects/searchEngine/searchEngine/spiders/parsed html docs')
    #create the file    
    parsedFile = open(filepath, "a")
    #print(text)
    parsedFile.write(text)
    parsedFile.close()