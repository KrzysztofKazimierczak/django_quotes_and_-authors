from quotesapp.models import ScrapData
from scrapmyside.items import ScrapedDataItem



class MyPipeline:

    def process_item(self, item, spider):
        if isinstance(item, ScrapedDataItem):
            data = ScrapData(choice=item['option'], dictionary=item['dictionary'])
            data.save()
        return item