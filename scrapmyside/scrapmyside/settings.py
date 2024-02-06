BOT_NAME = "scrapmyside"

SPIDER_MODULES = ["scrapmyside.spiders"]
NEWSPIDER_MODULE = "scrapmyside.spiders"


# Obey robots.txt rules
ROBOTSTXT_OBEY = False

ITEM_PIPELINES = {
    "scrapmyside.pipelines.MyPipeline": 300,
}
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"
