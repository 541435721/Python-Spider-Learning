# coding:utf-8
# __author__ = 'BianXuesheng'
# __data__ = '2016/04/19_18:49 '

from numpy import *
import re
import requests

url = 'http://tieba.baidu.com/f?fr=search&ie=utf-8&kw=%E5%8E%A6%E9%97%A8%E5%A4%A7%E5%AD%A6%E7%A0%94%E7%A9%B6%E7%94%9F%E9%99%A2'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36'}
html = requests.get(url, headers)
html.encoding = 'utf-8'

if __name__ == '__main__':
    rule = u'title="主题作者: (.*?)" data-field='
    out = re.findall(rule, html.text, re.S)
    # print html.text
    for i in out:
        print i
