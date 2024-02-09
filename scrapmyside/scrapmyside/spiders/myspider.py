import scrapy
from scrapmyside.items import ScrapedDataItem

class MySpider(scrapy.Spider):
    name = 'myspider'
    allowed_domains = ['localhost']
    start_urls = ['http://localhost:8000/']
    data_list = []


    def __init__(self, *args, **kwargs):
        super(MySpider, self).__init__(*args, **kwargs)
        self.data_to_scrap = kwargs.get('data_to_scrap', '').lower()

    def parse(self, response):

        for div_to_scrap in response.xpath("//div[@class='record']"):
            scrapped_data = div_to_scrap.xpath(".//span[@class='" + self.data_to_scrap + "']")
            if scrapped_data:
               for data in scrapped_data:
                    scrapped_data_text = data.xpath("string()").get().strip()
                    record = {self.data_to_scrap: scrapped_data_text}
                    if record not in self.data_list:
                        self.data_list.append(record)
        
        next_page = response.xpath("//a[@class='next']/@href").get()

        if next_page:
            next_page_url = response.urljoin(next_page)
            yield scrapy.Request(url=next_page_url, callback=self.parse)
        else:
            scrap_data_object = ScrapedDataItem(choice=self.data_to_scrap, dictionary=self.data_list)
            scrap_data_object.save()
            print("Done")
