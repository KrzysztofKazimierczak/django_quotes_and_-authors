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
        data_list = []
        for div_to_scrap in response.xpath("//div[@class='record']"):
            span_datas = div_to_scrap.xpath(".//span[@class='" + self.data_to_scrap + "']")
            scrapped_data_text = ','.join(span.xpath("string()").get().strip() for span in span_datas)
            data_list.append({self.data_to_scrap: scrapped_data_text})
        
        print(data_list)

