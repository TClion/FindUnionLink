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


def find_jd_union_link(html):
    jdurl = re.compile(r'https://union-click.jd.com/jdc\?d=')
    result = jdurl.search(html)
    if result:
        print 'This page have jd union link'



if __name__ == '__main__':
    url = "http://www.baidu.com"
    html = get_html(url)
    find_coinhive_js(html)
    find_jd_union_link(html)