import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        urls = [
            'https://www.whatismybrowser.com/',
            'http://icanhazip.com/',
            'http://useragentstring.com/'
        ]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = '{}.html'.format(page)
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)
