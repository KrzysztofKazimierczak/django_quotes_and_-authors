#from scrapy.spiders import CrawlSpider
import scrapy
from scrapmyside.items import ScrapedDataItem

class MySpider(scrapy.Spider):
    name = 'myspider'
    allowed_domains = ['localhost']
    start_urls = ['http://localhost:8000/']

    def __init__(self, *args, **kwargs):
        super(MySpider, self).__init__(*args, **kwargs)
        self.data_to_scrap = kwargs.get('data_to_scrap', '').lower()

    def parse(self, response):
        for div_to_scrap in response.css('div.record'):
            scrapped_data = div_to_scrap.css(f'span.{self.data_to_scrap}::text').getall()
            if scrapped_data:
                scrapped_data_text = ','.join(scrapped_data)
                yield ScrapedDataItem(data={self.data_to_scrap: scrapped_data_text})
