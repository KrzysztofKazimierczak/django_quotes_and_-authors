import scrapy


class MyspiderSpider(scrapy.Spider):
    name = "myspider"
    allowed_domains = ["localhost:8000"]
    start_urls = ["http://localhost:8000/"]

    def parse(self, response):
        pass
