import scrapy

class files_to_download(scrapy.Item):
    
    files = scrapy.Field()
    file_urls = scrapy.Field()
    title = scrapy.Field()



class QuotesSpider(scrapy.Spider):
    name = "library"

    def start_requests(self):
        urls = [
            'https://www2.census.gov/library/'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        # no ppt, html, doc, xls, xlsx, bmp, 
        formats = ['.png', 'jpeg', '.zip', '.gif', '.pdf', '.csv', 'pdf', 'jpg','.txt']
        hrefs = response.css('table a::attr(href)').extract()
        for link in hrefs:
            if link[0] != '?' and link[0] != '/':
                #print("orig link: " + link)
                full_link = str(response.url) + str(link)
                print("full link: " + full_link)
                if any(x in full_link.lower() for x in formats):
                    yield files_to_download(file_urls=[full_link], title=full_link[31:])
                else:
                    try:
                        yield scrapy.Request(url=full_link, callback=self.parse)
                    except Exception as e:
                        print("full_link")
