#!/usr/bin/env python
# coding=utf8

# version:1.0
# kali linux python 2.7.13
# author:TClion
# create:2018-12-12

import re
import sys
import requests


def get_html(url):
    try:
        html = requests.get(url).text
        return html
    except:
        print "Page cannot be accessed"
        sys.exit(0)


def find_coinhive_js(html):
    coinjs = re.compile(r'https://coinhive.com/lib/coinhive.min.js')
    result = coinjs.search(html)
    if result:
        print 'This page have coinhive code'


def find_2345_union_link(html):
    union_link = re.compile(r'http://www.2345.com/\?\d+')
    result = union_link.search(html)
    if result:
        print 'This page have 2345 union link'


def find_jd_union_link(html):
    jd = re.compile(r'https://union-click.jd.com/jdc\?d=')
    result = jd.search(html)
    if result:
        print 'This page have jd union link'


def find_taobaoke_union_link(html):
    taobaoke = re.compile(r'http://ai.taobao.com/\?pid=')
    result = taobaoke.search(html)
    if result:
        print 'This page have taobaoke union link'

if __name__ == '__main__':
    url = "http://www.baidu.com"
    html = get_html(url)
    find_coinhive_js(html)
    find_jd_union_link(html)
    find_2345_union_link(html)
    find_taobaoke_link(html)
