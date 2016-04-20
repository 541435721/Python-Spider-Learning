# coding:utf-8
# __author__ = 'BianXuesheng'
# __data__ = '2016/04/20_16:13 '

from numpy import *
import requests
from multiprocessing.dummy import Pool
from lxml import etree
import time


def getsource(url):
    html = requests.get(url)
    return html


urls = []
for i in xrange(10):
    urls.append(
        'http://tieba.baidu.com/f?kw=%E5%8E%A6%E9%97%A8%E5%A4%A7%E5%AD%A6%E7%A0%94%E7%A9%B6%E7%94%9F%E9%99%A2&ie=utf-8&pn=' + str(
            50 * i))

pool = Pool(6)

if __name__ == '__main__':
    start = time.time()
    for url in urls:
        getsource(url)
    print time.time() - start

    start = time.clock()
    result = pool.map(getsource, urls)
    print time.clock() - start
