import scrapy


class WeibospiderSpider(scrapy.Spider):
    name = "weiboSpider"
    allowed_domains = ["m.weibo.cn"]
    start_urls = ["https://m.weibo.cn"]

    def parse(self, response):
        pass
