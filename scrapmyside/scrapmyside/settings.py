BOT_NAME = "scrapmyside"

SPIDER_MODULES = ["scrapmyside.spiders"]
NEWSPIDER_MODULE = "scrapmyside.spiders"


# Obey robots.txt rules
ROBOTSTXT_OBEY = False

ITEM_PIPELINES = {
    "scrapmyside.pipelines.MyPipeline": 300,
}

"""REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
"""
FEED_EXPORT_ENCODING = "utf-8"


import django
import os
import sys
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), ""))
os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rest.settings')
os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"
django.setup()