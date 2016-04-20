# coding:utf-8
# __author__ = 'BianXuesheng'
# __data__ = '2016/04/20_15:37 '

from numpy import *
from lxml import etree
import requests

url = 'http://tieba.baidu.com/f?kw=%CF%C3%C3%C5%B4%F3%D1%A7%D1%D0%BE%BF%C9%FA%D4%BA&fr=index'
html = requests.get(url)
# html.encoding = 'utf-8'
# print html.text

selector = etree.HTML(html.text)
content = selector.xpath('//li[@class="j_thread_list clearfix"]/div/div[2]/div[1]/div[1]/a/text()')

if __name__ == '__main__':
    for i in content:
        print i

'''
//*[@id="thread_list"]/li[7]/div/div[2]/div[1]/div[1]/a
//*[@id="thread_list"]/li[12]/div/div[2]/div[1]/div[1]/a[2]
'''
