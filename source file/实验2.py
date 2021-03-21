# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 12:46:53 2020

@author: 10232
"""



import requests
import re 
# 写网站站点
url = "http://www.xbiquge.la/47/47061/"
# 写入headers模拟浏览器上网,避免出现个别网站拒绝访问的情况
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:67.0) Gecko/20100101 Firefox/67.0",}
# get发送请求
response = requests.get(url,headers=headers)
#将网页编码方式转换为utf-8
response.encoding = 'utf-8'
# 网站源码 
html = response.text
title =re.findall(r'<meta property="og:title" content="(.*?)"/>',html)[0]
fb = open('%s.txt' % title,'w',encoding ='utf-8')
# re.findall获取小说的名字

dl = re.findall(r'<div id="list">.*?</div>',html,re.S)[0]
chapter_info_list = re.findall(r"href='(.*?)' >(.*?)<",dl)

    
for chapter_info in chapter_info_list:
    chapter_url,chapter_title = chapter_info
    chapter_url="http://www.xbiquge.la%s" % chapter_url
    print(chapter_url,chapter_title)
    chapter_response=requests.get(chapter_url)
    chapter_response.encoding='utf-8'
    chapter_html=chapter_response.text
    chapter_content=re.findall(r'<div id="content">(.*?)</div>',chapter_html,re.S)[0]
    chapter_content=chapter_content.replace(' ','')
    chapter_content=chapter_content.replace('&nbsp;&nbsp;&nbsp;&nbsp;','')
    chapter_content=chapter_content.replace('<br />','')
    chapter_content=chapter_content.replace('<br/>','')
    chapter_content=chapter_content.replace('<p><ahref="http://koubei.baidu.com/s/xbiquge.la"target="_blank">亲,点击进去,给个好评呗,分数越高更新越快,据说给新笔趣阁打满分的最后都找到了漂亮的老婆哦!</a>手机站全新改版升级地址：http://m.xbiquge.la，数据和书签与电脑站同步，无广告清新阅读！</p>','')
    
    fb.write(chapter_title)
    fb.write('\n\n\n')
    fb.write(chapter_content)
    fb.write('\n\n\n')
    
    exit()
    
