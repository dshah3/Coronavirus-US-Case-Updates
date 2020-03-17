import scrapy
import json
import time
import requests
from datetime import datetime
from twisted.internet import reactor
from twisted.internet.task import deferLater
from scrapy.crawler import CrawlerProcess
from scrapy.utils.log import configure_logging
from scrapy.utils.project import get_project_settings

webhook_url = #use your own slack webhook

class CoronaVirusSpider(scrapy.Spider):
    name = "coronavirus"
    start_urls = [
        'https://www.worldometers.info/coronavirus/'
    ]

    def parse(self, response):

        dateTimeObj = datetime.now()
        timestampStr = dateTimeObj.strftime("%d-%b-%Y (%H:%M:%S.%f)")

        response = requests.post(webhook_url, json={
           'text': 'As of ' + timestampStr
           + ' Total Cases: ' + response.css("table td::text").extract()[71].encode('ascii','ignore') 
           + ' New Cases: ' + response.css("table td::text").extract()[72].encode('ascii','ignore') 
           + ' Total Deaths: ' + response.css("table td::text").extract()[73].encode('ascii','ignore')
           + ' New Deaths: ' + response.css("table td::text").extract()[74].encode('ascii','ignore')
        }, 
        headers={'Content-Type': 'application/json'})

        if response.status_code != 200:
            raise ValueError(
                'Request to slack returned an error %s, the response is:\n%s'
                % (response.status_code, response.text)
        )

def sleep(self, seconds, *args):
    return deferLater(reactor, seconds, lambda: None)

process = CrawlerProcess(get_project_settings())

def _crawl(result, spider):
    deferred = process.crawl(spider)
    deferred.addCallback(sleep, seconds=10800)
    deferred.addCallback(_crawl, spider)
    return deferred

_crawl(None, CoronaVirusSpider)
process.start()
    

    
    
