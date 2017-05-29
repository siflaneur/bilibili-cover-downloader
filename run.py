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
    headers = {
        'Cookie': 'sid=893sbj6c; fts=1492176047; rpdid=iwqskmlipxdoplikswwww; LIVE_BUVID=898b2fd420abdeed77e9f69d063922b6; LIVE_BUVID__ckMd5=7b23ba6e01913a93; buvid3=F84F9764-9FC8-4E40-978B-97F16E3D0F8D18602infoc; finger=493fd772; DedeUserID=18206016; DedeUserID__ckMd5=6b00b8789ffdd015; SESSDATA=c59cb004%2C1497490702%2Cf5b668d7; bili_jct=4c5df9cd55d5aacc9adf7f5f1d400500; UM_distinctid=15c155a5370b1-0dc7d5e8703b0a-5393662-bdd80-15c155a537151; html5_player_gray=false; pgv_pvi=2766686208; LIVE_LOGIN_DATA=4776b4f0ca9a1455df34ae0717f004bb1d90c1b6; LIVE_LOGIN_DATA__ckMd5=c1908ac1c4f2cb64; purl_token=bilibili_1495990055; _cnt_pm=0; _cnt_notify=0; user_face=http%3A%2F%2Fi1.hdslb.com%2Fbfs%2Fface%2F7cad65f532eae230a98bd4ecf6832168f5bbf319.jpg; _dfcaptcha=07256f5db1f6d882a0443c38198472b2',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
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
