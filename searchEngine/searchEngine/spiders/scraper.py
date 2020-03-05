import scrapy
from scrapy.http import Request
from englishScraper import English_Spider
import os
import csv

class StartSpider(scrapy.Spider):

    #name of the spider
    name = "start_Spider"
    #where spider will start crawling
    start_urls = ['https://www.cnn.com/us']

    urlName = " "
    count = 0

    #get urls based on selectors and extracts their text
    def parse(self, response):
        #gets content inside the div tag with class name cd__content
        urlContent = response.xpath('//div[@class="cd__content"]')
        countURL = 0
        #gets urls directly from the html file
        for urls in urlContent:

            #takes a single url from list of urls
            url = urls.xpath('.//a/@href').extract_first()

            #adds the baseurl to href urls that are from the base site
            fixedURL = response.urljoin(url[0:])

            #store url name globaly
            self.urlName = fixedURL

            if fixedURL is not None:
                #storenew_html(fixedURL, self.count)
                yield scrapy.Request(fixedURL, callback= self.parse_All_Text)
           
    #runs through the urls taken from the start url site
    def parse_All_Text(self, response):
        ur = response.request.url
        urlTexts = response.xpath('//body//div/text()').extract()
        urlTextsTwo = response.xpath('//body//div//p/text()').extract()
        urlTextsThree = response.xpath('//body//p/text()').extract()

        #create a new text file wih url inside     
        storenew_html(ur, self.count)
        
        #store all the text from the website on a text file
        if urlTextsThree is not None:
            append_html(''.join(urlTextsThree), self.count)
        if urlTextsTwo is not None:
            append_html(''.join(urlTextsTwo), self.count)
        if urlTexts is not None:
            append_html(''.join(urlTexts), self.count)
        
        
        self.count += 1

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
    
def generate_report(text, fileName, directoryPath, numberOfLinks):
    #combine filepath name with newly created file
    filepath = os.path.join(directoryPath, (str(fileName) + ".txt"))
    #checks if the directory exists
    if not os.path.exists(directoryPath):
         #if directory does not exist then create it
        os.makedirs(directoryPath)
    #create the file    
    parsedFile = open(filepath, "a")
    #print(text)
    parsedFile.write(text + '\n')
    parsedFile.write(numberOfLinks)
    parsedFile.close()


    
    
            
            