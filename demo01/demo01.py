# coding:utf-8
# __author__ = 'BianXuesheng'
# __data__ = '2016/04/19_15:48 '

import numpy as np
import re

if __name__ == '__main__':
    s = 'FGHxxIxxJKINBHKJYTKxxLOVExxUOIJJNGTYJOIMxxYOUxxLOHUYOGBILBLI'
    b = re.findall('xx(.*?)xx', s)
    c = re.search('xx(.*?)xx', s).group(1)
    b2 = re.findall('FGHxx(.*?)xxJKINBHKJYTKxx(.*?)xxUOIJJNGTYJOIMxx(.*?)xxLOHUYOGBILBLI', s)
    c2 = re.search('FGHxx(.*?)xxJKINBHKJYTKxx(.*?)xxUOIJJNGTYJOIMxx(.*?)xxLOHUYOGBILBLI', s).group(1)
    print b2, c2

    print re.sub('xx(.*?)xx', 'TTTTTTTTT', s)
    print re.sub('FGHxx(.*?)xxJKINBHKJYTKxx(.*?)xxUOIJJNGTYJOIMxx(.*?)xxLOHUYOGBILBLI', 'ttt', s)
