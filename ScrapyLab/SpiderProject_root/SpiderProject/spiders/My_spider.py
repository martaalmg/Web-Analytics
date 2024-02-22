import scrapy

class MySpider(scrapy.Spider):
    name = "MySpider"
    allowed_domains = ["www.uc3m.es"]
    start_urls = ["https://www.uc3m.es/bachelor-degree/data-science"]

    def parse(self, response):
        # Locate the link with text="Web Analytics"
        web_analytics_link = response.xpath('//a[contains(text(), "Web Analytics")]/@href').get()

        # Print it in the log
        self.log("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~> Web Analytics Link: " + web_analytics_link)
