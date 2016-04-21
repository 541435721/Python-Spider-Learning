# coding:utf-8
# __author__ = 'BianXuesheng'
# __data__ = '2016/04/20_21:57 '

from numpy import *
import scrapy


class DmozSpider(scrapy.spiders.Spider):
    name = "dmoz"
    allowed_domains = ["dmoz.org"]
    start_urls = [
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"
    ]

    def parse(self, response):
        print response.body
