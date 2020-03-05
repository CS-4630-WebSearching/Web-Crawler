import scrapy

class English_Spider(scrapy.Spider):

    name = "english spider"

    start_urls = ['www.google.com']

    def __init__(self, url = " "):
        self.start_urls = url



    def parse(self, response):

        #gets content inside the div tag with class name cd__content
        urlContent = response.xpath('//body//span')
        
        #gets urls directly from the html file
        for text in urlContent:
            #takes a single url from list of urls
            par = text.xpath('/text()').extract_first()
            
            print("THIS WORKED")
            #adds the baseurl to href urls that are from the base site
            #fixedURL = response.urljoin(url[1:])
            #s
