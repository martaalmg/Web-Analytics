import scrapy

class MySpider1(scrapy.Spider):
    name = "MySpider1"
    allowed_domains = ["aplicaciones.uc3m.es"]
    start_urls = ["https://aplicaciones.uc3m.es/cpa/generaFicha?&est=350&plan=392&asig=16507&idioma=2"]

    def parse(self, response):

        # Get the div that contains the Description title
        title_div = response.xpath('//div[@class="panel-heading degradado" and contains(text(), "Description of contents: programme")]')

        # Extract the following sibling div that contains the description
        description_div = title_div.xpath('./following-sibling::div[1]')

        # Extract the text inside the description div
        description_text = description_div.xpath('.//text()').getall()

        # Join and print in the log
        description = ''.join(description_text).strip()
        self.log("Description of Contents: " + description)