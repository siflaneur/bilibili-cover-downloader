# -*- coding: utf-8 -*-
# @Author: siflaneur
# @Date:   2017-05-29 01:05:48
# @Last Modified by:   siflaneur
# @Last Modified time: 2017-05-29 01:52:12


import re
import requests
import sys
from bs4 import BeautifulSoup


def downloader(av):
    url = 'http://www.bilibili.com/video/av' + av
    #  TODO
    headers = {
        'Cookie': 'your cookies',
        'User-Agent': 'your UA'
    }
    html = requests.get(url, headers=headers)
    bs = BeautifulSoup(html.text, 'html5lib')

    title = bs.title.text.split('_')[0]
    print(title)
    link = 'http:' + bs.body.img['src']

    tail = re.findall(".*(\.\w+)", link)[0]
    pic = 'cover' + str(tail)

    r = requests.get(link)
    if r.status_code == 200:
        with open(pic, 'wb') as f:
            f.write(r.content)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Please input av number')
    else:
        av = sys.argv[1]
        downloader(av)
