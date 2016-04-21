# coding:utf-8
# __author__ = 'BianXuesheng'
# __data__ = '2016/04/20_21:32 '

from numpy import *
from scrapy.contrib.spiders import CrawlSpider


class Douban(CrawlSpider):
    name = 'DoubanTest'
    start_urls = ['https://www.baidu.com/']

    def parse(self, response):
        print response.body
        print response.url

