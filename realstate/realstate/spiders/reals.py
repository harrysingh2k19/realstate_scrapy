import scrapy
from ..items import RealstateItem

class realstate(scrapy.Spider):
    name = 'posts'
    start_urls = ['https://www.housingwire.com/category/real-estate/']
    def parse(self, response):
        item = RealstateItem()
        test = []
        head = response.css('li.posts-list__item h3').css('::text').getall()
        link = response.css('li.posts-list__item a.entry-title').xpath('@href').getall()
        date = response.css('li.posts-list__item span.date-posted').css('::text').getall()
        item['title'] =head
        item['link'] =link
        item['date'] =date
        yield item
