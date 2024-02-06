import scrapy

class ScrapedDataItem(scrapy.Item):
    data = scrapy.Field()