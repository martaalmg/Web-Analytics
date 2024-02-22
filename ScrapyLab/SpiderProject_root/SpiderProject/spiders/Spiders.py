import sys
import os
import scrapy

# Add the path to your Scrapy project directory
scrapy_project_path = '/content/drive/MyDrive/WebAnalytics/SpiderProject_root/SpiderProject'
sys.path.append(scrapy_project_path)


from scrapy.crawler import CrawlerProcess
from spiders.My_spider import MySpider
from spiders.My_spider1 import MySpider1

if __name__ == "__main__":
    process = CrawlerProcess()
    process.crawl(MySpider)
    process.crawl(MySpider1)
    process.start()
    