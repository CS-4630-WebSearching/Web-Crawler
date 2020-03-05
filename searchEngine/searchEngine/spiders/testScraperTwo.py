import scrapy
from bs4 import BeautifulSoup
from scrapy.http import Request
from urllib.request import urlopen
import os
import csv

class StartSpider(scrapy.Spider):

      #name of the spider
    name = "start_Spider"
    #where spider will start crawling
    start_urls = ['https://www.cnn.com/us']

    urlName = " "
    count = 0
    linkCount = 0
    #get urls based on selectors and extracts their text
    def parse(self, response):
        #gets content inside the div tag with class name cd__content
        urlContent = response.xpath('*//a/@href').extract()

        #gets urls directly from the html file
        for urls in urlContent:
            #adds the baseurl to href urls that are from the base site
            fixedURL = response.urljoin(urls[0:])

            #store url name globaly
            self.urlName = fixedURL

            if fixedURL is not None:
                if self.count <= 10:
                #storenew_html(fixedURL, self.count)
                    yield scrapy.Request(fixedURL, callback=self.parse_All_Links)
    
    def parse_All_Links(self, response):
        ur = response.request.url
        directoryPath = "/Users/Bluck/Documents/Python Projects/searchEngine/searchEngine/spiders/report"
        directoryPathTwo = "/Users/Bluck/Documents/Python Projects/searchEngine/searchEngine/spiders/parsed html docs"
        links = response.xpath('*//a/@href').extract()
        linkCounter = 0

        #GET TEXT
        urlTexts = response.xpath('//body//div/text()').extract()
        urlTextsTwo = response.xpath('//body//div//p/text()').extract()
        urlTextsThree = response.xpath('//body//p/text()').extract()

        #create a new text file wih url inside     
        storenew_html(ur, self.count, directoryPathTwo)
        
        #store all the text from the website on a text file
        if urlTextsThree is not None:
            append_html(''.join(urlTextsThree), self.count, directoryPathTwo)
        if urlTextsTwo is not None:
            append_html(''.join(urlTextsTwo), self.count, directoryPathTwo)
        if urlTexts is not None:
            append_html(''.join(urlTexts), self.count, directoryPathTwo)    
        
        self.count += 1
        print(self.count)

        for link in links:
            if self.count <= 25:
                outf = open('htmlData.txt', 'a')
                
                fixedURL = response.urljoin(link[0:])
                if fixedURL is not None:
                    linkCounter += 1
                    outf.write(fixedURL + "\n")           
                    yield scrapy.Request(fixedURL, callback=self.parse_All_Links)
            generate_report(ur, "report", directoryPath, linkCounter)
            
#create the file for storing parsed html text
def storenew_html(text, fileName, directoryPath):
    #combine filepath name with newly created file
    filepath = os.path.join(directoryPath, (str(fileName) + ".txt"))
    #checks if the directory exists
    if not os.path.exists(directoryPath):
         #if directory does not exist then create it
        os.makedirs(directoryPath)
    #create the file    
    parsedFile = open(filepath, "w")
    parsedFile.write(text)
    parsedFile.close()

#append to the file for storing parsed html text
def append_html(text, fileName, directoryPath):
    #combine filepath name with newly created file
    filepath = os.path.join(directoryPath, (str(fileName) + ".txt"))
    #checks if the directory exists
    if not os.path.exists(directoryPath):
         #if directory does not exist then create it
        os.makedirs(directoryPath)
    #create the file    
    parsedFile = open(filepath, "a")
    #print(text)
    parsedFile.write(text)
    parsedFile.close()
    
def generate_report(text, fileName, directoryPath, numberOfLinks):
    #combine filepath name with newly created file
    with open((fileName + ".csv"), 'a') as csvfile:
        filewriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        filewriter.writerow([text, numberOfLinks])
