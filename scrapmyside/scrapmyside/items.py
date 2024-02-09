import scrapy
from scrapy_djangoitem import DjangoItem
from quotesapp.models import ScrapData


class ScrapedDataItem(DjangoItem):
    django_model = ScrapData
