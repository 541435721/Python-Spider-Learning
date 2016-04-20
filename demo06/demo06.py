# coding:utf-8
# __author__ = 'BianXuesheng'
# __data__ = '2016/04/20_16:40 '

from numpy import *
from lxml import etree
from multiprocessing.dummy import Pool
import requests

'''
爬取跟帖用户名， 跟帖内容，跟帖时间
'''

pool = Pool(6)
url = 'http://tieba.baidu.com/p/4184322822?pn='
page = 1

urls = []
for i in xrange(5):
    urls.append(url + str(i + 1))

comments = []


def getsource(url):
    html = requests.get(url)
    selector = etree.HTML(html.text)
    content = selector.xpath('//cc/div[starts-with(@id,"post_content_")]/text()')
    for i in content:
        i = i.replace('\n', '').replace('\t', '').strip()
    comments.extend(content)
    print url
    print len(content)
    print len(comments)


if __name__ == '__main__':
    # content = getsource(urls[0])
    pool.map(getsource, urls)
    for i in comments:
        print i
'''
//*[@id="post_content_79742208605"]
'''
