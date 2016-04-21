# coding:utf-8
# __author__ = 'BianXuesheng'
# __data__ = '2016/04/20_18:53 '

from numpy import *
import requests
from lxml import etree

# url = 'https://www.zhihu.com/explore'
url = 'https://www.zhihu.com/explore'
cook = {
    'Cookie': 'q_c1=ca02543dee0941349d594f671305ac20|1460352847000|1460352847000; d_c0="AEBAcbMHwQmPTvuV_8W47kUbXIzYo7auNro=|1460352847"; _za=19a9d4be-1497-4f8f-bd57-ef00495be247; _zap=57280031-8911-4d6f-a49f-1bb32667c233; _xsrf=e896bbcee0ead0e9b394a859e04315d5; l_n_c=1; l_cap_id="MGJiODE1ZDYxZWVmNGM5YmFmNzE5ZGRiZDU4MmFjMWE=|1461152337|6d3fff3a7629fabf382aff5e3aa8d51ece05402f"; cap_id="ZmNkOTUzMzAyOTA3NDZmZjkyNWNkNWViYTllNmEyMzc=|1461152337|5c91fb4a59257d78c15c470a7152418f256601da"; login="YTJhZDAxYmUyNDJlNGQ2Yjk5ZGI3N2VlYzNiY2M5OWI=|1461152359|dca0428f745830bb0be6987aa2ca608a0b1a3697"; z_c0="QUFCQXVQQXZBQUFYQUFBQVlRSlZUV2YzUGxmUGNjdlVjeWh6ZWkwcnFuOTBrc2ZGekF4WTRBPT0=|1461152359|7bff34a714946959231199aa77dcfee99c8231f2"; unlock_ticket="QUFCQXVQQXZBQUFYQUFBQVlRSlZUVzl4RjFkVERnZHJnaDlEdExkeHJEcGU4S1d5OGVoU2ZnPT0=|1461152359|287d46ea57fa045f2aab8502538189d07493661b'}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36'}

params = {"offset": '0', "type": "day"}

answers = {}

for i in xrange(1):
    page = str(i * 5)
    params["offset"] = page

    html = requests.get(url, headers, cookies=cook).text
    selector = etree.HTML(html)
    # question = selector.xpath('//div[@class="explore-feed feed-item"]/text()')
    ans = selector.xpath('//textarea/text()')
    for x in ans:
        print x[0:100]

if __name__ == '__main__':
    # for topic, ans in answers.items():
    #     print topic
    #     print ans
    #     print "__________________________________________________________________________________________________"
    pass
    # print html.text
