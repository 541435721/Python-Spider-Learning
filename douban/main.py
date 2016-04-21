# coding:utf-8
# __author__ = 'BianXuesheng'
# __data__ = '2016/04/20_21:41 '

from numpy import *
from scrapy import cmdline

if __name__ == '__main__':
    cmdline.execute("scrapy crawl DoubanTest".split())
