# coding:utf-8
# __author__ = 'BianXuesheng'
# __data__ = '2016/04/19_19:52 '

from numpy import *
import re
import requests

url = 'http://www.jikexueyuan.com/course/?pageNum='
page = 1

if __name__ == '__main__':
    for i in xrange(2):
        html = requests.get(url + str(page + i))
        html.encoding = 'utf-8'
        rule = u'<li id="\d{4}" test="0" deg="0" >(.*?)</li>'  # 爬取大框架
        out = re.findall(rule, html.text, re.S)
        rule1 = u'class="lessonimg" title="(.*?)" alt="'  # 爬取课程名称
        rule2 = u'<p style="height: 0px; opacity: 0; display: none;">(.*?)</p>'  # 爬取课程介绍
        rule3 = u'</i><em>(.*?)</em>'  # 爬取课程时间
        rule4 = u'i class="xinhao-icon\d?"></i><em>(.*?)</em>'  # 爬取课程等级
        rule5 = u'<em class="learn-number">(.*?)人学习</em>'  # 爬取课程人数
        for x in out:
            name = re.search(rule1, x, re.S)
            intr = re.search(rule2, x, re.S)
            t = re.search(rule3, x, re.S)
            level = re.search(rule4, x, re.S)
            n = re.search(rule5, x, re.S)
            if name != None:
                print name.group(1).strip()
            if intr != None:
                print intr.group(1).strip()
            if t != None:
                print t.group(1).strip()[:3]+t.group(1).strip()[-3:]
            if level != None:
                print level.group(1).strip()
            if n != None:
                print n.group(1).strip()
            print '___________________________________________________________________________'

                # print html.text
