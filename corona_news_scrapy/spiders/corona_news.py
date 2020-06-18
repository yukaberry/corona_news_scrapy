# -*- coding: utf-8 -*-
import scrapy
from corona_news_scrapy.items import CoronaNewsScrapyItem

class CoronaNewsSpider(scrapy.Spider):
    name = 'corona_news'
    #allowed_domains = ['https://www.deutschland.de/en/news/coronavirus-in-germany-informations']
    start_urls = ['https://www.deutschland.de/en/news/coronavirus-in-germany-informations/']

    def parse(self, response):
        for text in response.css('.story__content'):
            item =CoronaNewsScrapyItem()
            #import pdb; pdb.set_trace() # test
            item['text']=text.css('div.paragraph::text').extract_first()
            #item['span']=text.css('div.paragraph span::text').extract_first() this is not working
            item['header'] = text.css('h2::text').extract_first()
            #import ipdb; ipdb.set_trace() # test 
            yield item


