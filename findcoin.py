#!/usr/bin/env python
# coding=utf8

# version:1.0
# kali linux python 2.7.13
# author:TClion
# create:2018-12-12

import re
import requests


def find(url=None, html=None):
    try:
        html = requests.get(url).text
    except:
        print "Page cannot be accessed"
    coinpage = re.compile(r'https://coinhive.com/lib/coinhive.min.js')
    result = coinpage.search(html)
    if result:
        print 'This page have coinhive code'
    else:
        print 'safe html'


if __name__ == '__main__':
    url = "http://www.baidu.com"
    find(url)